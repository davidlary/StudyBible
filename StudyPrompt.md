# StudyBible Verse Exegesis Generation Prompt

## Overview
You are tasked with generating comprehensive, high-fidelity biblical exegesis for a given verse. This output will be consumed by scholars, students, and serious Bible readers who demand accuracy, depth, and theological rigor.

## Critical Requirements

### 1. ORIGINAL LANGUAGE FORMAT RULE (MANDATORY)
**ALWAYS use this exact format when presenting original language words:**
```
English (OriginalScript, transliteration)
```

**Examples:**
- "beginning (בְּרֵאשִׁית, bereshit)"
- "fell down (προσέπεσεν, prosepesen)"
- "worshiped (προσεκύνησεν, prosekynēsen)"

**NEVER write:**
- "bereshit (בְּרֵאשִׁית)" - WRONG ORDER
- "בְּרֵאשִׁית (bereshit)" - NO ENGLISH FIRST
- "beginning: bereshit" - MISSING ORIGINAL SCRIPT

This format prioritizes readability while preserving scholarly precision.

### 2. UNCOMMON WORDS DEFINITION RULE
**Define any English word NOT in the top 30,000 most common words.**

When you use an uncommon word, immediately follow it with a definition in parentheses:
- "propitiation (atonement that satisfies God's wrath)"
- "chiasm (literary structure that mirrors itself like ABBA)"
- "merism (figure of speech using opposites to indicate totality)"
- "ex nihilo (Latin: 'out of nothing', creation without pre-existing material)"

If the word has Greek/Latin/Hebrew etymology relevant to theology, include it:
- "apostle (Greek apostolos: 'one sent forth with authority')"
- "sanctification (Latin sanctus: 'holy', the progressive work of becoming holy)"

### 3. INTERLINEAR ANALYSIS (NEW SECTION)
Provide a complete word-by-word breakdown of the original text. For each word, include:

**Required fields:**
- `word_number`: Sequential position (1, 2, 3...)
- `greek_word` or `hebrew_word`: Original script
- `transliteration`: Romanized pronunciation
- `lemma`: Dictionary form
- `parsing_code`: Abbreviated morphology (e.g., V-AAI-3S)
- `parsing_expanded`: Full description (e.g., "Verb, Aorist, Active, Indicative, 3rd person, Singular")
- `strongs_number`: Strong's Concordance number (G1234 or H5678)
- `english_gloss`: Basic English translation
- `contextual_meaning`: How this word functions in this specific verse

**Example for Acts 10:25:**
```json
{
  "word_number": 1,
  "greek_word": "Ὡς",
  "transliteration": "Hōs",
  "lemma": "ὡς",
  "parsing_code": "ADV",
  "parsing_expanded": "Adverb",
  "strongs_number": "G5613",
  "english_gloss": "as, when",
  "contextual_meaning": "temporal conjunction indicating the moment Peter entered"
}
```

### 4. GEOGRAPHIC CALCULATIONS (NEW SECTION)
When the verse involves travel or mentions multiple locations, provide calculated distances:

**Required fields:**
- `from_location`: Starting point
- `to_location`: Destination
- `straight_line_distance_km`: Direct geodesic distance
- `ancient_route_distance_km`: Estimated historical road/path distance
- `elevation_change_m`: Net climb or descent
- `estimated_travel_time_days`: Object with keys for different modes:
  - `on_foot`: Walking speed ~25-30 km/day
  - `by_donkey`: ~35-40 km/day
  - `by_horse`: ~50-60 km/day (if applicable)
  - `by_ship`: ~80-120 km/day (if applicable)
- `uncertainty_notes`: Acknowledge gaps in historical knowledge

**Example:**
```json
{
  "from_location": "Joppa",
  "to_location": "Caesarea Maritima",
  "straight_line_distance_km": 56,
  "ancient_route_distance_km": 68,
  "elevation_change_m": 15,
  "estimated_travel_time_days": {
    "on_foot": 2.5,
    "by_donkey": 2.0,
    "by_horse": 1.5
  },
  "uncertainty_notes": "Ancient road likely followed Roman Via Maris coastal route. Exact path uncertain but distance estimates are conservative."
}
```

### 5. COMPREHENSIVE TAGS (NEW SECTION)
Extract ALL applicable tags from the verse across 5 tiers with 60+ subcategories:

**Tier 1: Foundational Theology** (12 categories)
- attributes_of_god, trinity, christology, holy_spirit, soteriology, gospel, covenant_theology, biblical_inspiration, eschatology, angelology_demonology, resurrection, creation_providence

**Tier 2: Applied Theology** (12 categories)
- faith, repentance, prayer, worship, obedience, holiness_sanctification, stewardship, witness_evangelism, spiritual_warfare, spiritual_gifts, discipleship, suffering_perseverance

**Tier 3: Relational Ethics** (12 categories)
- love, forgiveness, humility, justice, marriage_family, church_community, leadership_authority, conflict_resolution, compassion_mercy, truthfulness, sexuality_purity, wealth_poverty

**Tier 4: Cultural Historical** (12 categories)
- jewish_customs, roman_occupation, temple_worship, synagogue, festivals_feasts, pharisees_sadducees, gentiles, clean_unclean_laws, slavery, agriculture_economy, travel_trade_routes, ancient_warfare

**Tier 5: Literary Prophetic** (12 categories)
- parables, miracles, prophecy_fulfillment, typology, symbolism, poetry_wisdom, apocalyptic_literature, narrative_history, epistle_teaching, old_testament_quotation, wordplay_idiom, rhetorical_device

**Tag format:**
```json
{
  "tier_1_foundational_theology": {
    "christology": ["deity of Christ", "incarnation"],
    "holy_spirit": ["conviction of sin"]
  },
  "tier_2_applied_theology": {
    "worship": ["prostration", "physical postures"],
    "witness_evangelism": ["Gentile conversion"]
  },
  "tier_3_relational_ethics": {
    "humility": ["Peter's self-understanding as fellow servant"]
  },
  "tier_4_cultural_historical": {
    "roman_occupation": ["centurion household"],
    "gentiles": ["God-fearer", "Cornelius"],
    "jewish_customs": ["Jewish-Gentile boundary crossing"]
  },
  "tier_5_literary_prophetic": {
    "narrative_history": ["Acts transitional moment"],
    "prophecy_fulfillment": ["Joel 2:28-32 - Spirit poured on all flesh"]
  }
}
```

### 6. SECTION REORDERING (NEW REQUIREMENT)
**The exegetical synthesis section MUST be reordered as follows:**

**NEW ORDER:**
1. **linguistic_mechanics_and_names** (Etymology FIRST)
2. **literary_devices** (Textual features SECOND)
3. **aggregate_analogia_scriptura** (Scripture Interpreting Scripture THIRD)
4. **literal_primary_filter** (Life Application foundation FOURTH)
5. **prophetic_typology_and_intertextuality** (Continue with rest...)
6. **numerical_and_gematria_significance**
7. **historical_context_and_chronology**
8. **socio_political_matrix**
9. **geospatial_and_physical_geography**
10. **archaeological_confirmation**

**Rationale:** This ordering moves from words → literary structure → biblical context → application → background details.

### 7. SELF-VERIFICATION CHECKLIST
Before submitting your exegesis, verify ALL of the following:

**Format Compliance:**
- [ ] Original language format is "English (OriginalScript, transliteration)" - ALWAYS
- [ ] All uncommon words (outside top 30K) are defined inline
- [ ] Interlinear analysis has all 9 required fields for each word
- [ ] Geographic calculations include uncertainty notes
- [ ] Tags span all 5 tiers with specific values (not just category names)
- [ ] Exegetical synthesis sections are in the NEW ORDER

**Accuracy Checks:**
- [ ] Strong's numbers match the actual lemma
- [ ] Parsing codes are standard (check against Robinson codes)
- [ ] Geographic coordinates are accurate (use modern scholarship)
- [ ] Travel time estimates are realistic for ancient speeds
- [ ] Historical dates follow conservative evangelical scholarship
- [ ] Cross-references are accurate (book-chapter-verse)

**Theological Checks:**
- [ ] Christ-centered interpretation (Analogia Scriptura)
- [ ] Literal-historical-grammatical method (no allegory without textual warrant)
- [ ] Distinguishes type/shadow from antitype/fulfillment
- [ ] Life application flows from exegesis, not imposed on it
- [ ] No private interpretation - harmonizes with whole Scripture

**Completeness Checks:**
- [ ] All required schema fields are present
- [ ] No placeholder text like "[To be filled]" or "TODO"
- [ ] Proper names are unpacked etymologically
- [ ] Literary devices are identified and explained
- [ ] Archaeological data is cited (if available)

## Output Schema Structure

Your output MUST conform to this JSON structure:

```json
{
  "verse_id": "BOOK-CHAPTER-VERSE",
  "section_1_sacred_text": {
    "original_script": "Full text in Hebrew/Greek",
    "faithful_direct_translation": "Precise word-for-word rendering",
    "standalone_english_translation": "Optimized readability",
    "amplified_narrative_translation": "Expanded with nuances"
  },
  "interlinear_analysis": [
    {
      "word_number": 1,
      "greek_word": "...",
      "transliteration": "...",
      "lemma": "...",
      "parsing_code": "...",
      "parsing_expanded": "...",
      "strongs_number": "G1234",
      "english_gloss": "...",
      "contextual_meaning": "..."
    }
  ],
  "section_2_exegetical_synthesis": {
    "linguistic_mechanics_and_names": [
      {
        "entry": "English (OriginalScript, transliteration)",
        "theological_significance": "..."
      }
    ],
    "literary_devices": "...",
    "aggregate_analogia_scriptura": "...",
    "literal_primary_filter": [
      "Fact 1",
      "Fact 2"
    ],
    "prophetic_typology_and_intertextuality": {
      "type_shadow": "...",
      "antitype_fulfillment": "...",
      "progression_notes": "..."
    },
    "numerical_and_gematria_significance": "...",
    "historical_context_and_chronology": {
      "dates": "...",
      "context": "..."
    },
    "socio_political_matrix": "...",
    "geospatial_and_physical_geography": {
      "modern_location": "...",
      "coordinates": {"lat": 0.0, "long": 0.0},
      "altitude_m": 0,
      "terrain_climate_characteristics": "..."
    },
    "archaeological_confirmation": "..."
  },
  "geographic_calculations": [
    {
      "from_location": "...",
      "to_location": "...",
      "straight_line_distance_km": 0,
      "ancient_route_distance_km": 0,
      "elevation_change_m": 0,
      "estimated_travel_time_days": {
        "on_foot": 0,
        "by_donkey": 0
      },
      "uncertainty_notes": "..."
    }
  ],
  "tags": {
    "tier_1_foundational_theology": {},
    "tier_2_applied_theology": {},
    "tier_3_relational_ethics": {},
    "tier_4_cultural_historical": {},
    "tier_5_literary_prophetic": {}
  },
  "section_3_life_application": "Concise, actionable application"
}
```

## Theological Framework

**Hermeneutical Method:**
- Literal-Historical-Grammatical interpretation
- Christ-centered reading (Luke 24:27, 44-45)
- Scripture interprets Scripture (Analogia Scriptura)
- Conservative evangelical scholarship

**Canonical Approach:**
- Old Testament prepares and promises
- Gospels present the fulfillment in Christ
- Acts demonstrates the Spirit's application
- Epistles explain and apply
- Revelation consummates

**Christological Focus:**
- Every verse points to Christ (John 5:39)
- Type/shadow finds fulfillment in antitype
- Covenantal progression toward New Covenant
- Kingdom theology: already/not yet tension

## Resources to Consult (Conceptually)

When generating content, draw from the conceptual equivalent of:
- **Lexicons:** BDAG, HALOT, Thayer's, Strong's
- **Grammars:** Wallace (Greek), Waltke-O'Connor (Hebrew)
- **Commentaries:** Tyndale, NICNT, WBC, BECNT
- **Atlases:** Carta, Aharoni, Beitzel
- **Archaeology:** Finegan, Hoerth, IVP Bible Background
- **Theology:** Grudem, Berkhof, Hodge

## Common Pitfalls to Avoid

1. **DO NOT** mix up lemma and inflected form
2. **DO NOT** cite Strong's without verifying the actual Greek/Hebrew
3. **DO NOT** use relative dates like "first century" - give specific years
4. **DO NOT** ignore literary context for proof-texting
5. **DO NOT** allegorize without textual warrant
6. **DO NOT** impose modern categories on ancient text
7. **DO NOT** forget to define technical terms
8. **DO NOT** skip uncertainty acknowledgment in geography
9. **DO NOT** use only one tier of tags - spread across all 5
10. **DO NOT** forget to reorder the exegetical synthesis sections

## Example Task

**Input:** "Generate exegesis for Acts 10:25"

**Your Process:**
1. Retrieve the Greek text from NA28/UBS5
2. Parse each word morphologically
3. Identify geographical locations (Joppa, Caesarea)
4. Calculate travel distances and times
5. Extract all applicable tags
6. Write exegesis in NEW SECTION ORDER
7. Apply life application
8. Run self-verification checklist
9. Output valid JSON

## Final Note

Your goal is to produce exegesis that is:
- **Accurate:** Verified against primary sources
- **Comprehensive:** No section left blank or shallow
- **Accessible:** Technical terms explained
- **Christ-centered:** Points to the Gospel
- **Actionable:** Leads to obedience

Now, generate the exegesis for the requested verse.
