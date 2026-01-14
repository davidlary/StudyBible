"""
Tag Index Generator for StudyBible

Extracts tags from all verse JSON files and generates:
1. Flat index for fast searching (tag_index.json)
2. Category summaries (tag_categories.json)
3. Pagefind-compatible HTML data attributes

Author: Claude Sonnet 4.5
Date: 2026-01-14
"""

import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


class TagIndexer:
    """Generate search indexes from verse tags"""

    def __init__(self, data_path: str = "data"):
        self.data_path = Path(data_path)
        self.tag_index = []  # Flat list of {verse_id, category, value}
        self.category_index = defaultdict(set)  # Category -> Set of values
        self.verse_tags = {}  # verse_id -> all tags

    def index_all_verses(self):
        """Index all verses in data directory"""
        print("Indexing verses...")

        # Find all JSON files
        json_files = list(self.data_path.rglob("*.json"))
        print(f"Found {len(json_files)} verse files")

        for json_file in json_files:
            try:
                self._index_verse_file(json_file)
            except Exception as e:
                print(f"Error indexing {json_file}: {e}")

        print(f"Indexed {len(self.verse_tags)} verses")
        print(f"Found {len(self.tag_index)} total tag entries")

    def _index_verse_file(self, json_file: Path):
        """Index a single verse file"""
        with open(json_file, 'r', encoding='utf-8') as f:
            verse_data = json.load(f)

        verse_id = verse_data.get('verse_id', str(json_file.stem))

        # Extract tags if present
        tags = verse_data.get('tags', {})
        if not tags:
            return

        verse_tag_list = []

        # Process all tag categories
        for category, values in tags.items():
            if isinstance(values, dict):
                # Nested structure (e.g., people: {named_individuals: [...]})
                self._process_nested_tags(verse_id, category, values, verse_tag_list)
            elif isinstance(values, list):
                # Simple list of values
                for value in values:
                    self._add_tag_entry(verse_id, category, str(value), verse_tag_list)
            elif values:
                # Single value
                self._add_tag_entry(verse_id, category, str(values), verse_tag_list)

        self.verse_tags[verse_id] = verse_tag_list

    def _process_nested_tags(self, verse_id: str, parent_category: str, nested_dict: dict, verse_tag_list: list):
        """Process nested tag structures"""
        for subcategory, values in nested_dict.items():
            category_name = f"{parent_category}:{subcategory}"

            if isinstance(values, list):
                for value in values:
                    if isinstance(value, dict):
                        # Extract key information from objects
                        if 'name' in value:
                            self._add_tag_entry(verse_id, category_name, value['name'], verse_tag_list)
                        elif 'place' in value:
                            self._add_tag_entry(verse_id, category_name, value['place'], verse_tag_list)
                    else:
                        self._add_tag_entry(verse_id, category_name, str(value), verse_tag_list)
            elif values:
                self._add_tag_entry(verse_id, category_name, str(values), verse_tag_list)

    def _add_tag_entry(self, verse_id: str, category: str, value: str, verse_tag_list: list):
        """Add a tag entry to all indexes"""
        if not value or value == "None":
            return

        entry = {
            "v": verse_id,
            "cat": category,
            "val": value
        }

        self.tag_index.append(entry)
        self.category_index[category].add(value)
        verse_tag_list.append(f"{category}:{value}")

    def save_flat_index(self, output_path: str = "website/_data/tag_index.json"):
        """Save flat tag index for JavaScript filtering"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.tag_index, f, ensure_ascii=False, separators=(',', ':'))

        print(f"Saved flat index: {output_file} ({len(self.tag_index)} entries)")

    def save_category_summary(self, output_path: str = "website/_data/tag_categories.json"):
        """Save category summary for browsing UI"""
        output_file = Path(output_path)

        # Convert sets to sorted lists
        summary = {}
        for category, values in self.category_index.items():
            summary[category] = {
                "count": len(values),
                "values": sorted(list(values))
            }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"Saved category summary: {output_file} ({len(summary)} categories)")

    def save_verse_tags(self, output_path: str = "website/_data/verse_tags.json"):
        """Save per-verse tag lists for HTML data attributes"""
        output_file = Path(output_path)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.verse_tags, f, ensure_ascii=False, indent=2)

        print(f"Saved verse tags: {output_file} ({len(self.verse_tags)} verses)")

    def generate_statistics(self) -> Dict:
        """Generate indexing statistics"""
        stats = {
            "total_verses": len(self.verse_tags),
            "total_tag_entries": len(self.tag_index),
            "total_categories": len(self.category_index),
            "avg_tags_per_verse": len(self.tag_index) / max(len(self.verse_tags), 1),
            "categories": {}
        }

        for category, values in self.category_index.items():
            stats["categories"][category] = {
                "unique_values": len(values),
                "most_common": sorted(list(values))[:10]  # Top 10
            }

        return stats


def build_tag_indexes():
    """Main function to build all tag indexes"""
    indexer = TagIndexer()

    # Index all verses
    indexer.index_all_verses()

    # Save all indexes
    indexer.save_flat_index()
    indexer.save_category_summary()
    indexer.save_verse_tags()

    # Generate and save statistics
    stats = indexer.generate_statistics()
    with open("website/_data/tag_statistics.json", 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print("\n=== Tag Indexing Complete ===")
    print(f"Verses: {stats['total_verses']}")
    print(f"Tag Entries: {stats['total_tag_entries']}")
    print(f"Categories: {stats['total_categories']}")
    print(f"Avg Tags/Verse: {stats['avg_tags_per_verse']:.1f}")


if __name__ == "__main__":
    build_tag_indexes()
