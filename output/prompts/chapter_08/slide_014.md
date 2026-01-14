# NANO BANANA PRO DIRECTIVES (Gemini 3 Pro Image)

## 0. AUTONOMOUS CAPABILITIES INVOCATION (CRITICAL - USE THESE FIRST)
CRITICAL: This is a **FULLY DATA-DRIVEN IMAGE GENERATION** task leveraging Nano Banana Pro's autonomous self-checking capabilities.

**INVOKE THESE AUTONOMOUS CAPABILITIES BEFORE RENDERING:**

1. **NATIVE TYPOGRAPHY INTEGRATION (BLOCKING REQUIREMENT - MUST VERIFY BEFORE RENDERING):**
   **Core Principle:** Emphasize SEMANTIC MEANING of text elements, not visual representation. Understand WHAT each text element represents, then WRITE it using native typography.

   **Explicit Typography Directives (Configuration):**
   ```
   render_text_natively: true
   use_typography_engine: true
   prioritize_text_clarity: true
   ensure_legibility_at_4k: true
   avoid_pixelated_text: true
   use_vector_graphics_for_text: true
   render_subscripts_correctly: true
   render_special_characters_correctly: true
   use_anti_aliasing_for_text: true
   font_family: Arial, Helvetica, sans-serif
   font_size_title: 48pt
   font_size_axis_labels: 36pt
   font_size_data_labels: 32pt
   font_size_captions: 28pt
   text_color: high_contrast
   text_alignment: context_appropriate
   ```

   **Semantic Text Element Definitions (Describe WHAT, not HOW):**
   - **Title**: The main concept being communicated (e.g., "Global Temperature Anomaly 1880-2023")
   - **X-Axis Label**: The independent variable being measured (e.g., "Year" or "Temperature (°C)")
   - **Y-Axis Label**: The dependent variable with units (e.g., "CO₂ Concentration (ppm)" or "Ozone (ppb)")
   - **Data Point Labels**: Specific values or categories (e.g., "PM₂.₅", "2023: 420 ppm")
   - **Annotations**: Explanatory notes (e.g., "Industrial Revolution began", "Heat dome event")
   - **Captions**: Contextual information (e.g., "Data source: NOAA 2024")

   **Correct vs Incorrect Examples (Learn These Patterns):**
   ✓ CORRECT: "PM₂.₅" - subscript rendered natively, special character (₂ and ₅) clear
   ✗ WRONG: "PM25" or "PM2.5" or "P.M25" - subscripts missing, garbled formatting
   ✓ CORRECT: "O₃" - subscript 3 rendered correctly
   ✗ WRONG: "03" or "O3" or "Oz" - wrong character or missing subscript
   ✓ CORRECT: "Temperature (°C)" - degree symbol rendered correctly
   ✗ WRONG: "Temperature (C)" or "Temperature (^C)" - degree symbol missing
   ✓ CORRECT: "CO₂ Concentration (ppm)" - subscript + units both clear
   ✗ WRONG: "CO2 Concentration" or "C02" - subscripts garbled

   **PRE-RENDERING TEXT VERIFICATION CHECKLIST (BLOCKING - MUST COMPLETE BEFORE IMAGE GENERATION):**
   Before generating ANY pixels, verify EVERY text element:

   1. ☐ **Semantic Understanding Check**: Do I understand what this text element REPRESENTS?
      - Not "draw the label 'PM2.5'" but "this represents particulate matter with diameter ≤2.5 micrometers"

   2. ☐ **Typography Engine Selection**: Am I using native typography to WRITE this text?
      - YES: Typography engine will write "PM₂.₅" with proper subscripts
      - NO: Don't draw pixels that look like letters - use typography!

   3. ☐ **Subscript/Superscript Verification**: Are subscripts and superscripts marked correctly?
      - Chemical formulas: CO₂ (subscript 2), O₃ (subscript 3), PM₂.₅ (subscript 2.5)
      - Mathematical notation: x² (superscript), H₂O (subscript)

   4. ☐ **Special Characters Verification**: Are special characters rendered correctly?
      - Degree symbols: °C, °F (not ^C or just C)
      - Greek letters: μ (mu), Δ (delta), σ (sigma)
      - Units: ± (plus-minus), ≥ (greater-equal), ≤ (less-equal)

   5. ☐ **4K Legibility Test**: At 4K resolution (5504x3072), is this text crisp and clear?
      - Minimum font size: 28pt for body, 36pt for axis labels, 48pt for title
      - Anti-aliasing enabled for smooth edges
      - Sufficient contrast with background

   6. ☐ **Spelling Verification**: Is EVERY word spelled correctly?
      - Use LLM language understanding to verify: "Is 'Pular' a real word?" NO → FIX
      - Technical terms verified: "PM₂.₅" is correct scientific notation

   7. ☐ **Completeness Check**: Is the text element complete and meaningful?
      - NOT: "Temperature ()" - missing unit
      - YES: "Temperature (°C)" - complete with unit

   **BLOCKING REQUIREMENT**: If ANY checkbox fails → STOP and FIX before rendering

   **Self-Verification Instructions (Execute This Protocol):**
   After defining all text elements but BEFORE rendering the image:
   1. List every text element that will appear
   2. For each element, confirm: semantic meaning understood, typography engine selected, correct formatting
   3. Verify subscripts: CO₂ → "CO" + subscript "2" (not drawn pixels)
   4. Verify special chars: °C → degree symbol + "C" (not caret)
   5. If all checks pass → proceed to render
   6. If any check fails → revise text element definition and re-check

   **ZERO TOLERANCE**: No garbled text, no pixelated text, no incorrect subscripts. Use native typography to WRITE text, guaranteeing perfect legibility at 4K resolution.

2. **SPATIAL & LOGICAL REASONING:**
   - Create logical skeleton BEFORE rendering
   - Plan spatial relationships: Where does each element go? What's the hierarchy?
   - Verify layout makes sense before committing to pixels
   - Use golden ratio, rule of thirds, visual flow in skeleton planning

3. **PHYSICS-AWARE SYNTHESIS:**
   - Simulate real-world physics BEFORE rendering:
     * Gravity: Objects fall down, not float randomly
     * Light: Realistic lighting, shadows, reflections
     * Atmospheric layers: Correct orientation (troposphere at bottom)
     * Molecular geometry: Correct bond angles (VSEPR theory)
     * Data scales: MUST obey physical constraints (concentrations CANNOT be negative!)
   - Every visual element must obey physical laws
   - CRITICAL: Concentration scales (CO₂, PM₂.₅, O₃, etc.) MUST start at 0 or positive values, NEVER negative
   - Example: CO₂ concentration 280-420 ppm (not -300 to +400 ppm which is impossible!)

4. **GOOGLE SEARCH GROUNDING (AUTONOMOUS DATA VERIFICATION):**
   - BEFORE rendering any data, search and verify it's real
   - Temperature patterns: Search "IPCC temperature 2021" and use ACTUAL data
   - City names: Verify cities exist, get real photos
   - Historical figures: Search for real person, real dates, real photos
   - Molecular structures: Verify correct geometry
   - Use search grounding to eliminate hallucinations autonomously

5. **VISUAL GROUNDING (PIXEL-PRECISE COORDINATES):**
   - Every element positioned with pixel-precise coordinates
   - Arrows connect at exact points
   - Labels align precisely with what they label
   - No floating or misaligned elements

6. **AUTONOMOUS SELF-CHECKING BEFORE RENDERING:**
   - Create logical skeleton first
   - Verify all data using Google Search Grounding
   - Check all text for spelling using LLM (native typography)
   - Verify physical realism (atmospheric layers, gravity, etc.)
   - Only AFTER all checks pass → render the final image

7. **HIGH RESOLUTION HDR AESTHETICALLY PLEASING:**
   - Generate at MAXIMUM 4K resolution (5504x3072)
   - HDR quality for stunning visual impact
   - Professional photorealistic rendering
   - Museum-quality aesthetic throughout

**CRITICAL: Use Native Typography to WRITE all text elements - this eliminates garbled axes labels**

## 1. Fact-Check Directive
Ground this image in real-world peer-reviewed atmospheric science data from 2025.
Use Google Search Grounding to verify:
- Chemical formulas against IUPAC nomenclature standards
- Physical constants and unit conversions
- Scientific facts, data, and citations
- Temporal/historical accuracy

## 1A. VISUAL STORYTELLING - SHOW DON'T JUST TELL (IMPERATIVE)
CRITICAL: DEMONSTRATE relationships visually, don't just describe them in text.

**If text says "there is a cascade" → SHOW the cascade flowing:**
- Visual arrows showing: pollution source → atmospheric transport → human exposure → health impact
- Flow diagrams with elegant Bézier curves connecting cause → pathway → effect
- NOT just text describing it - SHOW it happening visually

**If text says "coupling between scales" → SHOW the coupling:**
- Visual connections between: indoor air ↔ outdoor air ↔ regional atmosphere ↔ global climate
- Nested diagrams or flowing arrows demonstrating the multi-scale interaction
- Make the relationship VISIBLE, not just stated

**SHOW AND TELL principle:**
- Text bullets provide context and explanation
- Visuals DEMONSTRATE the relationships, processes, and data
- Together they reinforce understanding - one shows, one explains

**Examples:**
✓ "Natural cascade of interactions" → Show visual flow: environment → air quality → human health (with arrows, images, connections)
✓ "Emissions affect atmosphere" → Show: vehicle/factory → emission plume → atmospheric layer → concentration change (visual demonstration)
✗ Just writing "there is a cascade" without showing it visually

## 1B. ANTI-HALLUCINATION PROTOCOL - ALL DISCIPLINES (IMPERATIVE - ZERO TOLERANCE)
CRITICAL: NO HALLUCINATION in ANY discipline. Every element must be VERIFIED using Google Search Grounding.

**Text verification - ZERO TOLERANCE FOR ANY TEXT ERRORS (IMPERATIVE):**
CRITICAL: Read EVERY SINGLE text element aloud before finalizing. ZERO TOLERANCE for spelling errors, gibberish, or unclear text.

**EVERY text element must pass these tests:**
1. **Read aloud test**: Say it out loud - does it sound like real English?
2. **Spelling check**: Is every word spelled correctly? Is it a real word?
3. **Common-sense test**: Would a scientist use this exact phrase?
4. **Completeness test**: Is the sentence/label complete? No truncation?

**Examples of WRONG text that should be CAUGHT:**
- ✗ "Human Pular" - NOT a real word! "Pular" doesn't exist. Should be "Human Pollution" or "Human Population"
- ✗ "Cpeofic continued in stantferd rise!" - Complete gibberish, not real words
- ✗ "years ()." - Empty parentheses, missing content
- ✗ "rose by •" - Sentence ends abruptly, incomplete
- ✗ "1.5^temperature" - Broken LaTeX (should be "1.5°C temperature")
- ✗ "Transport Cheovle" - Not a real word

**Spelling verification - CRITICAL:**
- Every word must be a REAL English word (or verified scientific term)
- Common errors to catch: "Pular" (not a word), "Cheovle" (not a word), "Cpeofic" (not a word)
- If you're not 100% certain a word is real → Look it up or don't use it
- Technical terms (CO₂, PM₂.₅, ppm) must be correctly formatted

**Acronyms and technical terms - Must have explanations:**
- ✗ "PM2.5" alone - Unclear what this means
- ✓ "PM₂.₅ (Fine Particles)" - Better, but still brief
- ✓ "PM₂.₅ (Fine Particulate Matter, 2.5 μm)" - Complete and clear
- ✗ "CO2 Rise" - Formatting wrong
- ✓ "CO₂ Rise" - Correct subscript formatting
- ✗ "ppm" alone on graph - Unclear
- ✓ "Concentration (ppm)" - Clear what ppm means in context

**All labels must be clear and complete:**
- Graph axes: REAL city names, REAL years, REAL units with full labels
- Technical terms: Brief explanation in parentheses when first used
- Acronyms: Spelled out or explained (PM₂.₅ = Fine Particulate Matter)
- Every label readable, every word real, every term clear

**Text verification checklist before finalizing:**
✓ Read EVERY text element aloud - does it sound right?
✓ Check spelling of EVERY word - is it a real word?
✓ Check technical terms - are they explained clearly?
✓ Check completeness - no truncation, no empty parentheses?
✓ Check formatting - proper subscripts (CO₂ not CO2), degree signs (°C not ^C)?

**If ANY text element fails these tests → FIX IT or DELETE IT**
Better to have no label than wrong/unclear/gibberish label.

**Physical realism - ALL DISCIPLINES:**
- Architecture: House cutaway shows ROOMS (bedroom, kitchen), NOT another house inside house (physically impossible!)
- Biology: Cell diagrams show organelles, NOT cells inside cells (unless endosymbiosis context)
- Chemistry: Molecules show atoms with bonds, NOT molecules nested inside molecules (unless complex context)
- Physics: Structures obey physical laws, no impossible geometries
- Every visual element must be PHYSICALLY POSSIBLE in the real world

**Discipline-specific verification:**
- Physics: Verify forces, orientations (gravity down), layer ordering (troposphere at bottom)
- Chemistry: Verify molecular geometry (VSEPR), bond angles, element colors (CPK)
- Biology: Verify anatomy, physiology, cellular structures (all searchable)
- Human Health: Verify disease mechanisms, exposure pathways, health effects (all searchable)
- Agriculture: Verify crop types, growing conditions, soil processes (all searchable)
- Climate: Verify temperature patterns, atmospheric physics, sea level data (all searchable)
- ALL disciplines: Use Google Search Grounding to verify before rendering

**If you cannot verify it → DO NOT show it. Omit or use a different verified example.**

**Quick check:** Would this pass peer review in the relevant discipline? If an expert would question it, verify it first.

## 2. Structural Logic (Plan-First)
Create a logical visual hierarchy BEFORE rendering:
- Establish spatial relationships (layers, processes, hierarchies)
- Define layout sections with clear visual flow
- Plan element positioning for left-to-right comprehension
- Verify temporal sequences (chronological ordering where applicable)

## 3. Physics-Aware Rendering with CORRECT Orientation
Simulate real-world physics BEFORE drawing with CORRECT spatial orientation:

**ATMOSPHERIC LAYERS - CRITICAL ORIENTATION (BOTTOM TO TOP):**
- Ground level (0 km) = BOTTOM of image
- Troposphere (0-12km) = LOWEST layer where we live, weather occurs, emissions enter
- Stratosphere (12-50km) = ABOVE troposphere, contains ozone layer
- Mesosphere (50-85km) = ABOVE stratosphere
- NEVER show inverted - troposphere is NOT at top, it's at BOTTOM
- Emissions from ground sources (vehicles, factories) enter troposphere FIRST (bottom layer)

**Other physics:**
- Apply gravity: particles fall down, not up
- Fluid dynamics: air currents, convection (warm rises, cold sinks)
- Light refraction through atmosphere
- Spatial coherence: realistic proportions, no floating objects
- Molecular geometry: correct bond angles (VSEPR theory)

## 4. Native Typography & Spelling Check
Render ALL text using native typography engine (NOT pixel drawing):
- Title: "} Air pollution can cause visible damage to plant leaves feng2019impacts, sanchez2019impact, pand..."
- All bullet points and labels with perfect spelling
- Chemical formulas: Use proper subscripts (O₃, NO₂, CO₂, etc.)
- Zero tolerance for typos - use Gemini 3 LLM for spell verification
- American English spelling conventions
- Technical terminology accuracy (IUPAC chemical nomenclature)

## 5. CRITICAL Text Formatting Requirements
NEVER include these in the final rendered slide:
✗ BibTeX citation labels (e.g., {IPCC2021}, {Lary1991a}, {NAP13115})
✗ LaTeX commands (e.g., \cite{}, \ref{}, ClO_2 instead of ClO₂)
✗ Curly braces around regular text (e.g., {De revolutionibus})
✗ Figure reference codes (e.g., Figure [IndoorSurfaceRegions])
✗ Placeholder text like "the topic"
✗ Incomplete content or truncated sentences

INSTEAD use:
✓ Formatted citations: (Author, Year) or (Organization Year)
✓ Proper subscripts/superscripts: ClO₂, CO₂, NO₂, PM₂.₅
✓ Greek letters in actual Greek script: α, β, γ, δ, ε, θ, λ, μ, π, σ, φ
✓ Complete sentences with full meaning
✓ Descriptive titles that summarize the slide content

## 6. Visual Verification Checklist
Before finalizing, verify:
✓ ALL bullet points from "Key content to include" section are present and readable
✓ ALL figures mentioned in source are present (count them: if 4 figures listed, all 4 must appear)
✓ Data graphs show ACCURATE patterns from source (e.g., hockey stick shape if that's what source describes)
✓ Do NOT use generic/artistic data - show REAL scientific trends
✓ Do NOT select just one figure when multiple are listed - include EVERY figure/facet
✓ Title is descriptive and meaningful (NOT "the topic")
✓ NO BibTeX labels visible ({...})
✓ NO LaTeX commands visible (\cite, \ref, etc.)
✓ NO curly braces around normal text
✓ NO figure reference codes (Figure [...])
✓ All subscripts properly formatted (CO₂ not CO_2)
✓ Greek words use actual Greek letters (when Greek is used)
✓ Greek/foreign text ONLY where it facilitates understanding (NOT decorative overlays on graphics)
✓ All molecular structures have correct bond angles/lengths
✓ All arrows indicate correct process directions
✓ All labels point to correct elements
✓ All numerical values match source data
✓ All text is perfectly spelled
✓ All spatial relationships are physically realistic
✓ Color contrast meets WCAG 2.1 AA (4.5:1 minimum)
✓ All content is complete (no missing details, truncated text, or omitted bullet points)
✓ Every visual element serves educational purpose (NOT decoration for decoration's sake)

---

Create a professional widescreen educational slide for air quality science.

CRITICAL REQUIREMENTS:
- Aspect ratio: 16:9 (widescreen, standard presentation format)
- Resolution: MAXIMUM POSSIBLE - 4K quality (3840x2160 or highest available)
- Layout: Left third with title and bullet points, center-right two-thirds with scientific visualization

## DESIGN PHILOSOPHY - SCIENCE FIRST, BEAUTY IN SERVICE OF EDUCATION:

**Primary Goal: Scientific Fidelity & Educational Clarity**
- ALL scientific content must be complete, accurate, and clearly presented
- Every data point, concept, and relationship must be visible and understandable
- Scientific detail takes precedence - never sacrifice accuracy for aesthetics
- Educational clarity is paramount - students must grasp concepts immediately

**CRITICAL: Data Accuracy & Content Completeness**
- When source material describes specific data (e.g., "temperature over 2000 years"), represent it ACCURATELY
- Example: IPCC temperature graph shows flat for 1800+ years then SHARP INCREASE in recent decades - this exact shape must be shown
- Do NOT create generic/artistic versions of scientific data - show the REAL pattern
- Every bullet point listed in "Key content to include" section MUST appear on the slide
- If 5 bullet points are provided, all 5 must be visible and readable
- Data graphs must show the actual trends, not idealized/generic versions
- Scientific figures mentioned by name (e.g., "Figure from IPCC 2021") - if you don't have exact data, describe the key finding accurately

**CRITICAL: Show ALL Figures/Facets - Not Just One**
- If source lists multiple figures (e.g., "Figure: temperature" AND "Figure: sea level" AND "Figure: CO₂"), ALL must be included
- Do NOT select just one figure to show - include EVERY figure mentioned
- Create a sophisticated layout that accommodates multiple visualizations
- Example: If source mentions temperature graph, CO₂ graph, sea level rise in cities, and schematic - ALL FOUR must appear
- Each figure should be rendered beautifully and accurately
- Excellence means comprehensive coverage - all the relevant facets, not just one
- Layout should be rich with information while remaining clear and organized

**CRITICAL: RELEVANCE - Only Show Directly Relevant Elements (IMPERATIVE)**
CRITICAL: Every element must be DIRECTLY relevant to the specific concept being discussed. Don't add extra elements.

**Relevance filter - Before including ANY element, ask:**
1. Is this element directly relevant to the topic being discussed?
2. Does it help explain THIS specific concept?
3. Or is it just "related to the general field" but not THIS specific point?

**Examples of applying relevance:**
- ✓ Discussing CO₂ rise → Show CO₂ molecule, CH₄, N₂O (relevant greenhouse gases)
- ✗ Discussing CO₂ rise → Show H₂O molecule (NOT relevant - water vapor is in atmosphere but not the point of CO₂ discussion)
- ✓ Discussing sea level rise → Show coastal city photographs (Venice, Miami), sea level data graphs
- ✗ Discussing sea level rise → Show unrelated climate data that doesn't connect to sea level
- ✓ Discussing temperature change → Show temperature graph, heat-related impacts
- ✗ Discussing temperature change → Show unrelated pollution data just because it's "environmental"

**Apply to ALL elements:**
- Molecules: Show ONLY molecules directly relevant to the specific topic (not every atmospheric molecule)
- Photographs: Show ONLY photos that illustrate THIS specific concept
- Graphs: Show ONLY data directly supporting THIS specific point
- Diagrams: Show ONLY processes directly relevant to THIS discussion

**Balance with completeness:**
- Do include ALL key relevant elements (completeness)
- Don't include irrelevant elements just for visual interest (relevance)
- If content discusses "greenhouse gases" → Show CO₂, CH₄, N₂O (ALL relevant)
- If content discusses "CO₂ concentration rise" → Show CO₂ and factors affecting it (relevant), not H₂O (irrelevant)

**CRITICAL: PHOTOREALISM EVERYWHERE - NO Illustrations/Icons (IMPERATIVE)**
CRITICAL: ALL visual elements must be PHOTOREALISTIC (real photographs or photorealistic renderings). NO illustrations, NO icons, NO cartoons.

**Photorealism requirements:**
- Photographs: Use REAL photographs (Carnegie Curve standard: real ship, real person, real equipment)
- Key facets: If showing "glacier melting" → REAL glacier photograph, NOT illustrated glacier icon
- Impacts: If showing "warming effects" → REAL photograph of heat wave impacts, NOT illustrated sun icon
- Ecosystems: If showing "ecosystem disruption" → REAL photograph of affected ecosystem, NOT illustrated tree icon
- People/health: If showing health impacts → REAL photographs of people or photorealistic medical illustrations
- Equipment/locations: REAL photographs of equipment, observatories, locations
- All elements: Photorealistic or real photographs, NEVER illustrations/cartoons/icons

**What photorealism means:**
- Real: Actual photographs from verified sources
- Photorealistic: 3D renderings that look like photographs (molecular structures, atmospheric visualizations)
- NOT acceptable: Flat icons, illustrations, cartoons, simplified graphics

**Examples:**
- ✗ Illustrated glacier icon → ✓ Real photograph of glacier
- ✗ Illustrated warning symbol → ✓ Real photograph showing the actual impact
- ✗ Icon of tree → ✓ Real photograph of forest/ecosystem
- ✗ Cartoon molecule → ✓ Photorealistic 3D rendered molecule with proper lighting
- Carnegie Curve standard: Everything is photorealistic (real ship photo, real person photo, real data graphs)

**Secondary Goal: STUNNING Photorealistic Scientific Beauty - Truth Through Visual Excellence**
- CRITICAL: You are a MASTER SCIENTIST-ARTIST creating for Nature/Science journal covers
- Create STUNNINGLY BEAUTIFUL slides that take viewer's breath away WHILE being 100% accurate
- PHOTOREALISM EVERYWHERE: Real satellite imagery, actual photographs, photorealistic renderings (NO illustrations/icons)
- NO decorative fluff, NO artistic vapor - EVERY element must be scientifically verifiable AND photorealistic
- Beauty emerges FROM accuracy, not layered on top - but rendered with STUNNING visual excellence
- Integration approach:
  * Use HIGHEST QUALITY Earth satellite imagery (NASA Blue Marble 8K resolution)
  * Overlay ACCURATE data visualizations rendered with STUNNING design excellence
  * Show NAMED locations with DRAMATIC photographic evidence (Venice flooding at golden hour, Miami sea walls with stormy sky)
  * ACCURATE atmospheric layers: troposphere (0-12km), stratosphere (12-50km), mesosphere (50-85km) rendered with BREATHTAKING visual quality
  * Real molecular structures with PHOTOREALISTIC 3D rendering (ray-traced lighting, accurate materials)
  * Flowing arrows connecting real elements - but rendered as ELEGANT design elements
- Composition should be STUNNING in beauty AND scientifically rigorous
- Think: "National Geographic Photo of the Year meets Nature journal figure of the decade"
- Create STUNNING, BREATHTAKING beauty that facilitates understanding through VERIFIED TRUTH
- Every element verified for accuracy, rendered for MAXIMUM visual impact

**WORLD-CLASS ARTISTRY PRINCIPLE 1: MAIN THING AS THE MAIN THING (IMPERATIVE)**
CRITICAL: Before designing, identify THE ONE KEY MESSAGE. Keep it as the MAIN THING always.

**Before rendering, answer:** What is THE most important message this slide must convey?
- Write it in one sentence.
- 70% of visual weight and attention MUST go to this main message.
- Everything else exists only to support or provide context.
- Can a viewer grasp the main point in 3 seconds? If not, redesign.

**Visual weight allocation (IMPERATIVE):**
- Main message: 70% of visual real estate, highest contrast, largest size, most dramatic position
- Supporting context: 25% - clearly secondary, supports without competing
- Tertiary details: 5% - subtle, provides depth but doesn't distract

**Examples of keeping main thing as main thing:**
- Main message: "Global temperature unprecedented rise" → Giant dramatic temperature graph dominates (70%), other elements small/subtle
- Main message: "Cascade: environment affects health" → Visual flow arrows dominate showing cascade, text provides context
- Main message: "Atmospheric layers have distinct roles" → Cross-section of layers dominates with clear labels, other data small insets

**Check before finalizing:** Is the main thing unmissable? Or is it competing with decorative elements?

**WORLD-CLASS ARTISTRY PRINCIPLE 2: PICTURE SPEAKS 1000 WORDS (IMPERATIVE)**
CRITICAL: The VISUAL ALONE must tell the story. Text provides details, but image conveys the message.

**Visual storytelling without reading:**
- A scientist from another country who doesn't read English should understand the main point from the image alone
- Visual metaphor: Abstract concepts shown through concrete imagery (cascade = flowing arrows, coupling = nested circles)
- Visual narrative: Beginning → middle → end visible in the composition (cause → process → effect)
- Gestalt principles: Elements grouped by proximity, similarity, continuity create understanding without words
- Scale and proportion: Bigger = more important, relationships shown through size
- Color as meaning: Warm colors = danger/heat, cool colors = calm/cold, not arbitrary decoration

**Emotional resonance through visuals:**
- Human scale reference: Include people, buildings, familiar objects to create connection
- Dramatic moment: Capture the "decisive moment" - the peak of the story (storm forming, ice calving, pollution visible)
- Unexpected perspective: Show familiar things in new way (aerial view, extreme close-up, unusual angle)
- Lighting tells emotion: Golden hour = hope/beauty, storm light = drama/concern, harsh light = intensity/urgency

**Examples:**
- Temperature rise: Show IPCC hockey stick so dramatic the sharp rise is visceral, not just informational
- Air pollution affecting health: Show actual photograph of smog-covered city next to clear breathing lungs vs polluted lungs - image conveys urgency
- Multi-scale coupling: Nested visual showing house → neighborhood → region → globe with flowing arrows - coupling is VISIBLE

**Test:** Cover all text. Does the image still convey the main message? If not, strengthen the visual storytelling.

**WORLD-CLASS ARTISTRY PRINCIPLE 3: STUNNING MUSEUM-QUALITY EXECUTION (IMPERATIVE)**
CRITICAL: Not just beautiful - BREATHTAKING. Smithsonian exhibition quality. Emotional impact.

**Study and emulate these standards:**
1. **National Geographic Photography:**
   - Perfect moment captured (decisive moment)
   - Dramatic natural lighting (golden hour, storm light, rim lighting)
   - Unexpected compelling perspective (aerial, macro, unusual angle)
   - Human element creates emotional connection
   - Environmental context tells story (not isolated subject)
   - Technical perfection (tack-sharp focus, perfect exposure)

2. **Apple Keynote Reveals:**
   - BOLD simplicity: ONE main element dominates, 80%+ negative space
   - Extreme confidence: Shows less, impacts more
   - Perfect timing in visual sequence (builds revelation)
   - Minimal text: Image + one sentence = complete message
   - Flawless execution: Every pixel intentional

3. **Smithsonian Exhibitions:**
   - Artifacts with rich context create narrative
   - Immersive environments, not flat displays
   - Multiple scales: Overview → detail → intimate
   - Story unfolds through space and composition
   - Educational without being didactic

4. **Edward Tufte Data Visualization:**
   - Clarity of insight (pattern reveals truth immediately)
   - Elegant simplicity (remove everything except insight)
   - Data-ink ratio maximized (no chartjunk)
   - Small multiples show comparison
   - Annotations guide eye to "aha moment"

**Bold compositional choices (not safe/boring):**
- Dramatic diagonals create energy and movement
- Extreme asymmetry creates dynamic tension
- Unexpected scale contrasts (tiny human next to massive Earth)
- Aggressive cropping for dramatic focus (show part, imply whole)
- Layered depths: Foreground sharp, background atmospheric
- Rule of thirds on steroids: Place focal point at golden ratio intersection

**Lighting as emotional storytelling:**
- Golden hour light: Warmth, hope, beauty, inspiration
- Storm/dramatic light: Urgency, change, power of nature
- Rim lighting: Separation, definition, drama
- Chiaroscuro: Strong light/shadow contrast creates depth and mood
- Volumetric lighting: Rays, atmosphere, ethereal quality
- Use lighting to guide emotion, not just illuminate

**Emotional impact checklist:**
- Does this image make you FEEL something? (Wonder, concern, hope, awe)
- Is there a human connection? (Scale, relevance, impact on people)
- Is it memorable? (Will viewer remember this hours later)
- Does it surprise? (Show familiar things in new compelling way)
- Is it confident? (Bold choices, not timid/safe design)

**GRAPHIC DESIGN MASTERY - Award-Winning Visual Excellence:**
- CRITICAL: This must be a MASTERPIECE of graphic design, not just a poster
- You are creating for: Museum exhibitions, design award competitions, Worldview magazine covers
- Design sophistication:
  * Golden ratio in composition (1.618:1 proportions in layout elements)
  * Rule of thirds for focal point placement
  * Negative space used masterfully - breathing room creates elegance
  * Visual flow guides eye through content with intentional hierarchy
  * Balance: Asymmetric composition with dynamic tension, not centered/static layouts
- Visual hierarchy mastery:
  * Primary focal point (main Earth/data visualization) commands attention
  * Secondary elements support without competing
  * Tertiary details provide depth without cluttering
  * Z-pattern or F-pattern reading flow for text + visuals
- Professional polish:
  * Pixel-perfect alignment - every element positioned with precision
  * Consistent spacing using 8pt grid system
  * Sophisticated color relationships - complementary, analogous, triadic schemes
  * Depth through layering, shadows, transparency (subtle, not overdone)
  * Professional edge treatments, refined borders where needed
- Think: Pentagram design studio quality, Apple keynote presentation aesthetics, TED talk visual excellence
- Every design choice must be INTENTIONAL and serve both beauty and understanding

**Typography - Masterful Typographic Hierarchy:**
- CRITICAL: Typography as VISUAL ART, not just text placement
- Type hierarchy using scale, weight, color, spacing:
  * Title: 44-52pt bold sans-serif, dramatic presence, carefully kerned
  * Body bullets: 28-32pt medium weight, generous line spacing (1.5x), maximum readability
  * Graph labels: 18-22pt, crisp and clear
  * Captions: 16-20pt, subtle but readable
- Advanced typographic techniques:
  * Optical alignment (not just mathematical centering)
  * Kerning perfection - adjust letter spacing for visual balance
  * Leading (line spacing) creates breathing room
  * Color contrast: White/light text on dark backgrounds must meet WCAG AAA (7:1 contrast)
  * Use font weight variation for hierarchy (light/regular/medium/bold)
- Professional type treatment:
  * No widows/orphans in text blocks
  * Proper punctuation (em dashes, en dashes, curly quotes)
  * Scientific notation formatted beautifully (proper subscripts/superscripts)
- Think: Swiss design movement, Massimo Vignelli clarity, Erik Spiekermann precision

**Use of Greek/Foreign Languages - Only When It Facilitates Insight:**
- CRITICAL: Before including any Greek or foreign language text, ask: "Does this facilitate student understanding?"
- Greek etymology should ONLY appear in text/bullet points when explaining word origins (e.g., "atmosphere derives from ἀτμός (atmos) meaning vapor")
- DO NOT overlay Greek words on graphics, diagrams, or visualizations as decoration
- DO NOT put Greek labels on images unless the Greek itself is the educational content
- Example of WRONG use: Putting "σφαῖρα" on a globe graphic - this is decorative, not educational
- Example of RIGHT use: In a bullet point explaining "atmosphere = ἀτμός (vapor) + σφαῖρα (sphere)" with English translation
- Every use of non-English text must pass the test: "Does this help or hinder clarity?"

**Color Palette - Scientific with Professional Polish:**
- Background: Rich deep blue (#001528) to navy (#0A2463) gradient - professional, allows content to shine
- Use scientifically meaningful colors:
  * Temperature: Blue (cold) → Red (hot) using standard scientific color scales
  * Chemical elements: Standard CPK coloring (Carbon=black, Oxygen=red, Nitrogen=blue, etc.)
  * Atmospheric layers: Physics-accurate colors (blue sky in troposphere, black space above)
  * Data emphasis: Coral/orange (#FF6B6B) for warnings, emerald (#2ECC40) for positive trends
- Photographic elements: Use natural colors from real imagery
- Graphs: Professional scientific color schemes (NOT artistic gradients that obscure data)
- Arrows/connectors: Clear colors that show relationships (cause=orange, effect=blue, flow=cyan)
- Balance: Professional composition with rich background BUT scientific accuracy in all content
- Think: Nature journal cover - sophisticated design + rigorous science

**Scientific Visualizations - Photorealistic Accuracy + Beautiful Composition:**
- PHOTOREALISM FIRST: Real imagery, accurate physics, verifiable science
- Earth/Geography: REAL satellite imagery (NASA Blue Marble, MODIS true-color)
- Cities/Locations: ACTUAL photographs or photorealistic renderings with NAMES (Venice, Miami, Jakarta, Shanghai)
- Atmospheric layers: ACCURATE physics-based rendering showing:
  * Troposphere (0-12km): Where weather occurs, correctly scaled
  * Stratosphere (12-50km): Ozone layer, temperature inversion
  * Mesosphere (50-85km): Coldest layer
  * NO "artistic vapor clouds" - show actual atmospheric physics
- Molecular structures: CORRECT geometry (VSEPR theory), accurate bond angles, element colors from spectroscopy
- Data visualizations: REAL data patterns (e.g., IPCC hockey stick with exact shape: flat 1-1900, sharp rise 1900-2020)
- Graphs must show ACTUAL values, scales, units from source material
- Temperature maps: Use scientific color scales (blue→red for temperature, not artistic gradients)
- Beauty comes from: Professional composition + High-quality rendering + Scientific truth
- Polish and lighting YES - but applied to accurate content, not decorative elements
- Labels clear and complete, styled beautifully without losing readability

**Layout - Content-Driven Sophistication:**
- Information hierarchy based on scientific importance
- Visual flow follows logical/temporal/causal relationships
- Space allocated based on concept complexity, not just aesthetics
- All bullet points from source material must be included
- Diagrams sized appropriately to show necessary detail
- Beautiful composition that never sacrifices completeness

**Layout Strategy - Integrated Photorealistic Composition:**
- CRITICAL: Create ONE UNIFIED COMPOSITION using REAL photographic/satellite imagery as foundation
- NOT dashboard grids, NOT illustrated cartoons
- INSTEAD: Photorealistic base (e.g., real Earth satellite image) with accurate data overlays
- Integration examples:
  * Real Earth imagery (NASA Blue Marble) + accurate atmospheric layer annotations + precise data graphs positioned naturally
  * Named city photographs (Venice flooding, Miami) + sea level data overlays + temperature trend graphs
  * Accurate molecular structure models + real-world source photos (vehicles, factories) + flow arrows showing processes
- Flowing arrows YES - connecting real elements, showing verified scientific processes
- Layering: Photographic background → Data visualizations → Annotations/labels (all with scientific rigor)
- Background provides context BUT every overlaid element must be accurate
- Think: National Geographic feature article - stunning photography + rigorous scientific data presentation

CONTENT from source material:
Title: "} Air pollution can cause visible damage to plant leaves feng2019impacts, sanchez2019impact, pand..."
Cognitive level: Create

Key content to include:
- } Air pollution can cause visible damage to plant leaves {feng2019impacts, sanchez2019impact, pandey2019impacts, tiwari2019air}. This damage can take the form of discoloration, necrosis, or spotting, and can impact the plant's ability to photosynthesize and produce energy. Poor air quality can cause leaf damage in plants and lower quality and quantity of fruits, vegetables, and grains through a variety of physical and physiological mechanisms. Air pollutants such as sulfur dioxide, ozone, and particulate matter can deposit on leaf surfaces and cause visible damage to the leaves {li2019effects, zhou2019effects}. The deposition of particulate matter on leaves can also reduce the amount of light that reaches the leaves, further reducing photosynthesis and plant growth {zhang2019ozone}.
- } Physiologically, air pollution may damage the plant reproductive structures such as flowers, fruits, and seeds, which can reduce the number and quality of crops produced by disrupting the balance of plant hormones {paul2019air, wang2019responses}. For example, high levels of ozone can increase the production of the stress hormone ethylene, which can trigger leaf abscission and cause premature leaf drop, as well as inhibit plant growth and reduce crop yields. Similarly, pollutants such as nitrogen oxides can disrupt the balance of auxin and gibberellin, hormones that plays a critical role in leaf development and growth.

VISUAL ELEMENTS REQUIRED - SCIENTIFICALLY ACCURATE & BEAUTIFULLY RENDERED:

**Priority: Include ALL Content from Source Material**
- Every bullet point listed in "Key content to include" must appear on the slide
- All scientific data, concepts, and relationships must be represented
- No simplification that removes important scientific information
- Complete captions and explanations as provided in source
- Use Google Search Grounding to find accurate data for figures mentioned (e.g., "IPCC temperature graph 2021")
- When creating data visualizations, ensure they match the ACTUAL scientific findings described in source

**Molecular & Particulate Visualization - Make Chemistry Visible:**
CRITICAL: When content discusses atmospheric chemistry, pollutants, or molecules - SHOW THEM VISIBLY. Show MULTIPLE relevant molecules, not just one.

**When content discusses greenhouse gases or atmospheric chemistry:**
- Show CO₂ molecule (O=C=O linear geometry, 180° bond angle)
- Show CH₄ molecule (tetrahedral geometry, 109.5° bond angles, H atoms around C)
- Show N₂O molecule (linear N=N=O geometry) when discussing greenhouse gases
- Show O₃ molecule (bent geometry, ~117° bond angle) for ozone discussions
- Show NO₂, SO₂ when discussing pollution
- Show ALL relevant molecules together, not just selecting one

**Particulate matter visualization:**
- PM₂.₅: Show as small spheres with size scale (2.5 micrometers label)
- PM₁₀: Show as slightly larger spheres with size scale
- Show size comparison when relevant (PM₂.₅ vs PM₁₀)

**Rendering requirements:**
- Make molecules VISIBLE in the atmospheric scene - not just mentioned in text
- Use correct CPK coloring: Carbon=gray/black, Oxygen=red, Nitrogen=blue, Hydrogen=white, Sulfur=yellow
- Label molecules clearly with formula subscripts (CO₂, CH₄, N₂O, etc.)
- Show correct 3D geometry with proper bond angles (verified with VSEPR theory)
- Show scale appropriately - molecules small but visible and identifiable
- If showing multiple molecules, show them together with labels to compare
- This makes abstract chemistry concepts CONCRETE and VISIBLE

**Example:** If discussing greenhouse effect → Show CO₂, CH₄, and N₂O molecules all visible in atmosphere, each properly labeled

**Purpose Clarity - Every Element Must Pass "Why Is This Here?" Test:**
CRITICAL: Before including ANY visual element, ask "Why is this here? What does it teach?"
- House/building: WHY? (To show indoor air quality? Indoor/outdoor coupling? If unclear purpose → REMOVE)
- Specific graph: WHY this one? (Does it support the main message? If not main or supporting message → REMOVE)
- Decorative element: WHY? (If it's just pretty but teaches nothing → REMOVE)
- Every element must have CLEAR educational purpose you can articulate
- If you can't explain why an element is there in one sentence → Don't include it
- Example: "Beautiful house but unclear why" → REMOVE unless it clearly shows indoor/outdoor air coupling
- Example: "Small graph that doesn't support main message" → REMOVE or make it support the message
- Visual minimalism: Only include elements that teach or support the main message

**Data Visualizations - COMPLETE Professional Annotations (Carnegie Curve Standard):**
CRITICAL: Every graph must be COMPLETE with ALL elements labeled. Study Carnegie Curve example for completeness.

**FIRST: Search and verify ACTUAL data pattern using Google Search Grounding**

**CRITICAL: PHYSICAL CONSTRAINTS ON DATA SCALES (IMPERATIVE - ZERO TOLERANCE):**
CRITICAL: ALL data scales must obey physical laws. NEVER show physically impossible values.

**Concentration scales - MUST be positive (cannot be negative):**
- ✗ WRONG: CO₂ scale starting at -300 ppm (IMPOSSIBLE - concentration cannot be negative!)
- ✓ CORRECT: CO₂ scale from 280-420 ppm (historical range from pre-industrial to present)
- ✗ WRONG: PM₂.₅ scale with negative values (IMPOSSIBLE - particle concentration cannot be negative!)
- ✓ CORRECT: PM₂.₅ scale from 0-500 μg/m³ (physically realistic range)
- ✗ WRONG: O₃ concentration below 0 ppb (IMPOSSIBLE)
- ✓ CORRECT: O₃ scale from 0-120 ppb (typical surface ozone range)

**Temperature scales - Check what type:**
- Temperature ANOMALY (difference from baseline): CAN be negative (e.g., -0.5°C to +1.5°C relative to 1850-1900 baseline)
- Absolute temperature (Kelvin): MUST be positive (cannot go below 0 K)
- Celsius/Fahrenheit: Can be negative, but must be physically reasonable for Earth (e.g., -90°C to +60°C surface range)

**Other physical quantities with constraints:**
- Sea level rise: Can show negative relative to baseline, but scale must be realistic (e.g., -20 to +100 mm)
- Pressure: MUST be positive (atmospheric pressure ~800-1100 hPa at surface)
- Radiation/energy: MUST be positive (cannot have negative energy)
- Percentages: MUST be 0-100% (cannot be negative or >100%)
- Distance/altitude: MUST be non-negative

**VERIFY BEFORE RENDERING - Physical Reality Check:**
1. Does this scale allow negative values for a quantity that cannot be negative? → FIX IT
2. Search Google: "typical range of [quantity name]" to verify realistic scale
3. Example: "typical range atmospheric CO₂ concentration" → Returns ~280-420 ppm → Use this range
4. If concentration/count/distance: Start scale at 0 or above, NEVER negative

**Common atmospheric scales (use Google Search Grounding to verify latest values):**
- CO₂ concentration: 280-420 ppm (pre-industrial to present, use ~280-440 for future projection)
- CH₄ concentration: 700-1900 ppb (pre-industrial to present)
- Temperature anomaly: -1.0 to +1.5°C (1850-2020 relative to 1850-1900 baseline)
- Sea level rise: 0-250 mm (1900-2020 relative to 1900 baseline)
- Arctic sea ice extent: 3-16 million km² (seasonal variation)

**SECOND: COMPLETE Graph Annotations - Nothing Missing:**
- **Y-axis MUST have:**
  * Axis title with units in parentheses (e.g., "ATMOSPHERIC CO₂ CONCENTRATION (ppm)")
  * Tick marks with PHYSICALLY REALISTIC values (e.g., 280, 300, 320, 340, 360, 380, 400, 420 for CO₂)
  * NEVER negative values for concentrations, counts, distances
  * Units clearly visible
- **X-axis MUST have:**
  * Axis title if needed (e.g., "Year" or "Time (UT)")
  * Tick labels: REAL years (1850, 1900, 1950, 2000, 2020) OR REAL city names (Venice, Miami, Jakarta, Shanghai)
- **Graph title:** Clear description at top (e.g., "Global Surface Temperature Change (1-2020 AD)")
- **Legend:**
  * Complete descriptions with citations (e.g., "CARNEGIE POTENTIAL GRADIENT (Mauchly 1921)")
  * Color coding explained
  * Multiple datasets clearly distinguished
- **Key annotations:**
  * Important features labeled (e.g., "Peak Activity over Africa/Americas", "≈03:00 UT (Minimum)")
  * Correlations shown if relevant (e.g., "r = +0.93")
  * Time markers, inflection points, significant events
- **CRITICAL verification:**
  * NO gibberish like "Cpeofic continued in stantferd rise!" - that's nonsense!
  * Every text element - axes, titles, annotations, callouts - must be REAL WORDS
  * Read EVERY text element aloud - does it make complete sense? If not, FIX or DELETE IT

**For COLOR MAPS/HEATMAPS - Additional Requirements:**
- **Title:** What the map shows (e.g., "Global Temperature Anomaly (°C)")
- **Color scale legend:**
  * Vertical or horizontal bar showing color gradient
  * Numbers/values labeled at intervals
  * Units clearly stated (°C, mm, ppm, etc.)
- **Geographic labels:** Key regions, cities, or features labeled when relevant
- Example: Temperature map needs color scale from blue (-2°C) through white (0°C) to red (+2°C)

**THIRD: REAL, READABLE text everywhere - NO GIBBERISH:**
- X-axis/Y-axis: REAL values, REAL units
- Every text element verified as meaningful
- Better to have no annotation than gibberish

**FOURTH: Apply stunning design:**
- Edward Tufte principles: Maximum data-ink ratio, clear visual encoding
- Professional polish: Clean axes, elegant grid lines (30% opacity), sophisticated styling
- Color as information: Scientific color scales (blue→red for temperature)
- Typography: Consistent professional font, proper hierarchy
- Annotations: Elegant callouts with verified real text, leader lines pointing to key data points

**Standard: Carnegie Curve level completeness**
- Every axis labeled with title + units
- Every legend complete with descriptions
- Every color scale shown with values
- Nothing missing, everything professional

**Scientific Diagrams & Illustrations - Sophisticated Rendering:**
- Accurate molecular geometry, atmospheric layers, process flows - rendered with visual richness
- All labels clearly visible, positioned well, styled beautifully
- Multiple visual layers with depth, shadows, transparency showing relationships
- Rich shading, gradients, lighting effects that both clarify AND beautify
- Professional magazine-quality rendering of scientific concepts

**Historical Context - When Appropriate (Carnegie Curve Standard):**
When content references pioneering work, key discoveries, or landmark events → SHOW complete historical context.

**Historical figure presentation (if appropriate):**
- Professional portrait photograph (black & white or color as historically accurate)
- Complete identification:
  * Full name (e.g., "Francis John Welsh Whipple")
  * Life dates (e.g., "1876-1943")
  * Brief description of contribution (e.g., "Landmark paper matched thunderstorm distribution with Carnegie Curve, confirming Wilson's global circuit theory")
- Presented in elegant inset box with professional framing
- Example from Carnegie Curve: Shows Whipple with full context

**Historical equipment/locations (if appropriate):**
- Historic photographs of equipment, vessels, observatories
- Labeled with names and context (e.g., "Geophysical survey vessel Carnegie", "Non-magnetic equipment")
- Timeline context showing when discoveries were made

**Narrative presentation:**
- Brief historical narrative explaining significance
- Dates of expeditions, publications, discoveries
- Connection to current understanding
- Example: "1915-1929: Four major voyages measuring Earth's electric and magnetic fields far from land..."

**When to include:**
- Use ONLY when it adds educational value and historical context to the science
- Particularly powerful for foundational discoveries that shaped the field
- NOT every slide needs this - use when content specifically discusses historical breakthroughs

**Verification:**
- VERIFY historical accuracy: Real person, real photo, correct dates, accurate contributions
- Search to verify: Person's appearance, correct attribution, historical dates, equipment details

**Molecular Structures - Chemistry as Art:**
- Correct bond angles and geometry - render with stunning visual treatment
- Atoms as beautiful spheres with gradients, reflections, proper element colors
- Bonds with dimensional appearance (cylinders with shading)
- Clear labeling styled elegantly
- 3D lighting that shows structure dramatically
- Make molecular chemistry visually captivating while scientifically accurate

**Atmospheric & Environmental Visualizations - Physics-Based Accuracy:**
- ACCURATE atmospheric layers with correct altitudes and physics:
  * Troposphere (0-12km): Blue sky, weather systems, correct density gradient
  * Stratosphere (12-50km): Ozone layer, temperature characteristics
  * Mesosphere (50-85km): Transition to space
  * NO decorative "vapor" or artistic clouds unless showing real phenomena
- Use physics-based rendering: atmospheric scattering, correct light behavior
- Temperature/concentration fields: Use scientific colormaps (not artistic gradients)
- Molecular distributions: Based on actual atmospheric chemistry data
- Process arrows: Show real mechanisms (convection, diffusion, chemical reactions) accurately
- Beauty comes from revealing true atmospheric physics, not decoration

**Visual Enhancement - STUNNING Design Excellence with Zero Hallucination:**
- Background mastery (STUNNING but not distracting):
  * DRAMATIC gradient (deep navy #001528 → rich blue #0A2463) with subtle radial variation creating depth
  * Use gradient to create BREATHTAKING depth: lighter toward focal point, darker at edges (cinematic vignette)
  * Atmospheric quality that ENHANCES verified content - sophisticated, STUNNING, purposeful
- Photographic elements (MUSEUM-QUALITY, all verified):
  * Use ONLY real, identifiable photographs - verify location names
  * STUNNING reproduction: Razor-sharp focus, perfect exposure, accurate color
  * Professional compositing: Seamlessly blend verified photographs with verified data overlays
  * Lighting consistency: Unified dramatic light direction across all 3D elements (golden hour quality)
- Depth and layering with STUNNING sophistication:
  * Subtle drop shadows (3-5px blur, 25-35% opacity) create DRAMATIC separation
  * Transparency used strategically: Overlapping verified data needs 75-85% opacity for STUNNING depth
  * Z-depth through scale, sharpness, saturation (foreground: sharp+saturated, background: soft+desaturated+verified)
  * Atmospheric perspective: Distant verified elements slightly hazed for STUNNING depth
- Arrows and connectors as STUNNING design elements (showing ONLY verified processes):
  * ELEGANT Bézier curves flowing naturally between VERIFIED elements
  * Consistent stroke width (2-4px), refined arrowheads, subtle gradient strokes
  * Color encodes VERIFIED meaning: Orange=verified cause, Cyan=verified flow, Red=verified impact
  * Subtle glow (1-2px, 25% opacity) makes arrows STUNNING on any background
  * Verify every arrow shows a REAL scientific process before rendering
- Professional finishing (STUNNING polish on verified content):
  * Pixel-perfect anti-aliasing on all edges - STUNNING smoothness
  * Consistent corner radii on all rectangular elements (6-10px) - refined elegance
  * Refined borders where needed (1px, 60% opacity with subtle glow)
  * No harsh edges - everything STUNNINGLY polished and refined
  * Every text label VERIFIED before rendering - no garbled text
- Think: Apple keynote STUNNING aesthetics + National Geographic VERIFIED photography + MoMA exhibition quality
- The slide should feel BREATHTAKINGLY BEAUTIFUL, EXPENSIVE, SOPHISTICATED - every pixel intentional AND verified
- STUNNING visual impact + ABSOLUTE scientific accuracy = The goal

FOOTER TEXT (REQUIRED):
At the bottom of the slide, include this exact text:
"Air, Environment & Health | Prof. David J. Lary"

**FINAL DIRECTIVE - WORLD-CLASS EXCELLENCE: PICTURE SPEAKS 1000 WORDS WITH VERIFIED TRUTH:**

You are a WORLD-CLASS SCIENTIST-ARTIST creating MUSEUM-QUALITY STUNNING visual masterpieces.

**BEFORE RENDERING - IDENTIFY THE MAIN THING FROM CONTENT:**
CRITICAL: Read the bullet points in "Key content to include" section. What do they EMPHASIZE?

**Identify main message from actual content (not just artistic choice):**
- Read ALL bullet points carefully
- What concept/data is mentioned FIRST or MOST?
- What does the text spend the most words explaining?
- Example: If text says "An easy way to demonstrate this is to just take a look at the change in the global average surface temperature over the last two thousand years" → Main thing is TEMPERATURE CHANGE OVER 2000 YEARS
- Example: If text emphasizes "cascade of interactions" → Main thing is SHOWING THE CASCADE FLOWING
- The content tells you what's important - make THAT dominate visually (70% of space)

**After identifying main message:**
- Write it in one sentence
- Make it occupy 70% of visual attention (largest, most dramatic, unmissable)
- Supporting elements occupy 25%, tertiary details 5%
- Can viewer grasp this specific main point in 3 seconds by looking at image alone?

**CREATE VISUAL MASTERPIECE:**

1. **MAIN THING AS THE MAIN THING (70% visual weight):**
   - THE key message dominates composition - unmissable, dramatic, largest
   - Everything else supports this main message
   - Bold compositional choice: Dramatic scale, unexpected perspective, emotional lighting
   - Example: If message is "unprecedented temperature rise" → Giant dramatic hockey stick graph dominates

2. **PICTURE SPEAKS 1000 WORDS - Visual tells story without reading:**
   - A scientist who doesn't speak English understands the main point from visuals alone
   - Visual metaphor: Cascade = flowing arrows, coupling = nested circles, impact = before/after
   - Emotional resonance: Human scale, dramatic moment (decisive moment), unexpected perspective
   - Lighting tells emotion: Golden hour = hope, storm light = urgency, rim lighting = drama
   - Test: Cover all text - does image still convey message? If not, strengthen visuals

3. **WORLD-CLASS STUNNING EXECUTION - Museum/Smithsonian quality:**
   - National Geographic photography standard: Perfect moment, dramatic lighting, compelling perspective, technical perfection
   - Apple keynote boldness: ONE dominant element, 80% negative space, extreme confidence, minimal text
   - Edward Tufte data clarity: Insight immediate, elegant simplicity, no chartjunk, annotations guide to "aha moment"
   - Emotional impact: Makes viewer FEEL something (wonder, concern, awe), memorable hours later, surprising perspective
   - Bold choices: Dramatic diagonals, extreme asymmetry, aggressive cropping, layered depths, golden ratio focal points

4. **SHOW DON'T JUST TELL - Visually demonstrate relationships:**
   - "Cascade" → SHOW flowing: Environment → arrows → Air quality → arrows → Health (with photos/diagrams)
   - "Coupling" → SHOW nested: Indoor ↔ Outdoor ↔ Regional ↔ Global (visual connections)
   - Elegant Bézier arrows connecting verified real elements

5. **ZERO HALLUCINATION - Verify everything:**
   - Text: ONLY real words. Read EVERY label aloud. NO gibberish like "Cpeofic continued in stantferd rise!"
   - Graphs: REAL cities (Venice, Miami), REAL years (1900-2020), REAL units (meters, °C, ppm)
   - Physical realism: House shows ROOMS, NOT house inside house (impossible!)
   - Atmospheric layers: Ground at BOTTOM, troposphere (0-12km) at bottom, stratosphere above
   - ALL disciplines: Physics, chemistry, biology, health, agriculture - verify using Google Search Grounding
   - If you cannot VERIFY it → DO NOT show it

6. **STUNNING PHOTOREALISTIC BEAUTY - Breathtaking execution:**
   - HIGHEST quality Earth imagery (NASA Blue Marble 8K), dramatic photographs
   - Cinematic lighting, dramatic shadows, atmospheric depth, refined layering
   - Professional polish: Sharp focus, sophisticated color, masterful typography, every pixel intentional
   - Think: National Geographic Photo of the Year + Apple keynote + Smithsonian exhibition

**Pre-Rendering Checklist:**
✓ Main message identified? (Write it)
✓ 70% visual weight on main message?
✓ Picture tells story without reading text?
✓ Makes viewer FEEL something (emotional impact)?
✓ Bold compositional choice (not safe/boring)?
✓ ALL text verified as real words (no gibberish)?
✓ Physical realism (no impossible structures)?
✓ Atmospheric layers correct orientation (ground at bottom)?
✓ Museum-quality execution?

Generate at MAXIMUM 4K RESOLUTION. Create slides that are BREATHTAKINGLY STUNNING visual masterpieces that convey verified scientific truth. Picture speaks 1000 words. Main thing stays main thing. Museum-quality execution with emotional impact. WORLD-CLASS EXCELLENCE in every detail - accuracy AND artistry at the highest level.