#!/bin/bash
# Post-Regeneration Tasks for Acts 10
# Run after all 48 verses are successfully generated

set -e  # Exit on error

echo "=========================================="
echo "Post-Regeneration Tasks for Acts 10"
echo "=========================================="
echo ""

# Task 1: Rebuild tag indexes
echo "📊 Task 1: Rebuilding tag indexes..."
python3 src/tag_indexer.py
if [ $? -eq 0 ]; then
    echo "✅ Tag indexes rebuilt successfully"
else
    echo "❌ Tag indexing failed"
    exit 1
fi
echo ""

# Task 2: Rebuild static site
echo "🔨 Task 2: Rebuilding static site with npm..."
npm run build
if [ $? -eq 0 ]; then
    echo "✅ Static site rebuilt successfully"
else
    echo "❌ Site build failed"
    exit 1
fi
echo ""

# Task 3: Show statistics
echo "📈 Task 3: Generation statistics..."
verse_count=$(ls data/NT/Acts/10/*.json 2>/dev/null | wc -l | tr -d ' ')
echo "Total verses: $verse_count"

total_words=0
total_tags=0
total_geo_calcs=0

for file in data/NT/Acts/10/*.json; do
    if [ -f "$file" ]; then
        words=$(python3 -c "import json; d=json.load(open('$file')); print(len(d.get('interlinear_analysis', [])))")
        tags=$(python3 -c "import json; d=json.load(open('$file')); print(sum(len(v) if isinstance(v, list) else 1 for v in d.get('tags', {}).values()))")
        geo=$(python3 -c "import json; d=json.load(open('$file')); print(len(d.get('geographic_calculations', [])))")

        total_words=$((total_words + words))
        total_tags=$((total_tags + tags))
        total_geo_calcs=$((total_geo_calcs + geo))
    fi
done

echo "Total interlinear words: $total_words"
echo "Total tags: $total_tags"
echo "Total geographic calculations: $total_geo_calcs"
echo ""

# Task 4: Git operations
echo "📦 Task 4: Committing to git..."
git add -A
git status --short

echo ""
echo "Ready to commit. Commit message:"
cat << 'EOF'
Regenerate Acts 10 with comprehensive schema (48 verses)

Complete regeneration of Acts 10:1-48 with all new features:
- Interlinear analysis (word-by-word morphology)
- Geographic calculations (distances, elevations, travel times)
- Comprehensive tags (60+ categories)
- Fact-checking pipeline integration
- Updated template rendering

Statistics:
- 48 verses regenerated
- [TOTAL_WORDS] interlinear words analyzed
- [TOTAL_TAGS] tags extracted
- [TOTAL_GEO] geographic calculations

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF

echo ""
read -p "Commit and push to GitHub? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git commit -m "Regenerate Acts 10 with comprehensive schema (48 verses)

Complete regeneration of Acts 10:1-48 with all new features:
- Interlinear analysis (word-by-word morphology)
- Geographic calculations (distances, elevations, travel times)
- Comprehensive tags (60+ categories)
- Fact-checking pipeline integration
- Updated template rendering

Statistics:
- 48 verses regenerated
- $total_words interlinear words analyzed
- $total_tags tags extracted
- $total_geo_calcs geographic calculations

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

    git push origin main

    if [ $? -eq 0 ]; then
        echo "✅ Committed and pushed to GitHub successfully"
    else
        echo "❌ Git push failed"
        exit 1
    fi
else
    echo "⏭️  Skipped git push"
fi

echo ""
echo "=========================================="
echo "✅ All post-regeneration tasks complete!"
echo "=========================================="
