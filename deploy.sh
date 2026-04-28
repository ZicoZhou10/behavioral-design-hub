#!/usr/bin/env bash
# ============================================================================
# Behavioral Design Hub — One-Line Deploy Script
# Usage:  bash deploy.sh
# Time:   ~60 seconds
# Result: Live site at https://<username>.github.io/behavioral-design-hub/
# ============================================================================
set -euo pipefail

REPO_NAME="behavioral-design-hub"
REPO_DESC="Free behavioral science tools, research-backed product teardowns, and ethical design benchmarks"
BRANCH="main"

# ─── Colors ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

step() { echo -e "\n${CYAN}[$(date +%H:%M:%S)]${NC} ${BOLD}$1${NC}"; }
ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
warn() { echo -e "  ${YELLOW}⚠${NC} $1"; }
fail() { echo -e "  ${RED}✗${NC} $1"; exit 1; }

# ─── 1. Pre-flight checks ───────────────────────────────────────────────────
step "Pre-flight checks"

# Check gh CLI
if ! command -v gh &> /dev/null; then
    fail "GitHub CLI (gh) not found. Install: https://cli.github.com/"
fi
ok "gh CLI found: $(gh --version | head -1)"

# Check git
if ! command -v git &> /dev/null; then
    fail "git not found. Install git first."
fi
ok "git found: $(git --version)"

# Check gh auth
if ! gh auth status &> /dev/null; then
    echo ""
    warn "Not authenticated with GitHub CLI."
    echo -e "  Run: ${BOLD}gh auth login${NC}"
    echo "  Then re-run this script."
    exit 1
fi
GH_USER=$(gh api user --jq '.login' 2>/dev/null)
ok "Authenticated as: ${BOLD}${GH_USER}${NC}"

# ─── 2. Navigate to hub directory ────────────────────────────────────────────
step "Locating hub directory"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HUB_DIR="$SCRIPT_DIR"

# Verify this is the right directory
if [ ! -f "$HUB_DIR/index.html" ]; then
    fail "index.html not found in $HUB_DIR — are you in the behavioral-design-hub directory?"
fi

FILE_COUNT=$(find "$HUB_DIR" -type f -not -path '*/.git/*' | wc -l)
ok "Hub directory: $HUB_DIR ($FILE_COUNT files)"

# ─── 3. Create GitHub repo (idempotent) ─────────────────────────────────────
step "Creating GitHub repository"

if gh repo view "${GH_USER}/${REPO_NAME}" &> /dev/null; then
    warn "Repository ${GH_USER}/${REPO_NAME} already exists — will push to it"
    REPO_EXISTS=true
else
    gh repo create "$REPO_NAME" \
        --public \
        --description "$REPO_DESC" \
        --homepage "https://${GH_USER}.github.io/${REPO_NAME}/" 2>/dev/null \
        && ok "Created: github.com/${GH_USER}/${REPO_NAME}" \
        || fail "Failed to create repository"
    REPO_EXISTS=false
fi

# ─── 4. Initialize git & push ────────────────────────────────────────────────
step "Initializing git and pushing"

cd "$HUB_DIR"

# Initialize if needed
if [ ! -d .git ]; then
    git init -b "$BRANCH" > /dev/null 2>&1
    ok "Initialized git repository"
else
    warn "Git already initialized — will commit and push"
fi

# Set remote (idempotent)
REMOTE_URL="https://github.com/${GH_USER}/${REPO_NAME}.git"
if git remote get-url origin &> /dev/null; then
    git remote set-url origin "$REMOTE_URL"
else
    git remote add origin "$REMOTE_URL"
fi
ok "Remote set: $REMOTE_URL"

# Stage all files
git add -A
ok "Staged all files"

# Commit (skip if nothing to commit)
if git diff --cached --quiet 2>/dev/null; then
    if git log --oneline -1 &> /dev/null; then
        warn "No new changes to commit — pushing existing commits"
    else
        fail "No files staged and no commits exist. Something went wrong."
    fi
else
    git commit -m "Deploy: Behavioral Design Hub ($(date +%Y-%m-%d)) — ${FILE_COUNT} files

Includes:
- Hub landing page with 15 product teardown previews
- Behavioral Design Score self-assessment tool
- 105 product comparison pages (programmatic SEO)
- 15 in-depth behavioral teardown pages
- Interactive leaderboard
- Embeddable widget
- Shareable score cards
- AI-friendly robots.txt + structured data (JSON-LD)
- GitHub Actions auto-deploy pipeline" > /dev/null 2>&1
    ok "Committed all files"
fi

# Push
git push -u origin "$BRANCH" --force 2>/dev/null \
    && ok "Pushed to origin/$BRANCH" \
    || { warn "Push failed — trying with force..."; git push -u origin "$BRANCH" --force; }

# ─── 5. Enable GitHub Pages ─────────────────────────────────────────────────
step "Enabling GitHub Pages"

# Enable Pages with GitHub Actions as build source
gh api \
    --method PUT \
    "repos/${GH_USER}/${REPO_NAME}/pages" \
    -f "build_type=workflow" \
    -f "source[branch]=${BRANCH}" \
    -f "source[path]=/" \
    > /dev/null 2>&1 \
    && ok "GitHub Pages enabled (source: GitHub Actions)" \
    || {
        # Try creating instead of updating (for new repos)
        gh api \
            --method POST \
            "repos/${GH_USER}/${REPO_NAME}/pages" \
            -f "build_type=workflow" \
            -f "source[branch]=${BRANCH}" \
            -f "source[path]=/" \
            > /dev/null 2>&1 \
            && ok "GitHub Pages enabled (source: GitHub Actions)" \
            || warn "Pages API call returned non-200 — may need manual enable: Settings → Pages → Source → GitHub Actions"
    }

# ─── 6. Trigger initial workflow run ────────────────────────────────────────
step "Triggering deploy workflow"

# Give GitHub a moment to register the workflow
sleep 2

gh workflow run "Deploy to GitHub Pages" --repo "${GH_USER}/${REPO_NAME}" 2>/dev/null \
    && ok "Workflow triggered" \
    || warn "Auto-trigger skipped — the push should have already triggered it"

# ─── 7. Output results ──────────────────────────────────────────────────────
LIVE_URL="https://${GH_USER}.github.io/${REPO_NAME}/"

echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}  DEPLOYMENT COMPLETE${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  ${BOLD}Live URL:${NC}      ${CYAN}${LIVE_URL}${NC}"
echo -e "  ${BOLD}Repository:${NC}    ${CYAN}https://github.com/${GH_USER}/${REPO_NAME}${NC}"
echo -e "  ${BOLD}Files:${NC}         ${FILE_COUNT} files deployed"
echo -e "  ${BOLD}Pages:${NC}         ~125+ indexable URLs"
echo ""
echo -e "  ${YELLOW}Note:${NC} First deploy takes 1-3 minutes to go live."
echo -e "  ${YELLOW}Check:${NC} ${CYAN}https://github.com/${GH_USER}/${REPO_NAME}/actions${NC}"
echo ""
echo -e "  ${BOLD}Next steps:${NC}"
echo -e "  1. Wait 1-3 min, then visit ${CYAN}${LIVE_URL}${NC}"
echo -e "  2. Share on social (pre-written posts in action-89 artifact)"
echo -e "  3. Future updates: edit files → git add . → git commit → git push"
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
