const fs = require('fs');
const path = require('path');

module.exports = function() {
  const verses = [];
  const dataDir = path.join(__dirname, '../../data/NT/Acts/10');

  // Check if directory exists
  if (!fs.existsSync(dataDir)) {
    console.warn('Acts 10 data directory not found:', dataDir);
    return verses;
  }

  // Read all JSON files in Acts 10 directory
  for (let i = 1; i <= 48; i++) {
    const verseFile = path.join(dataDir, `${String(i).padStart(2, '0')}.json`);

    if (fs.existsSync(verseFile)) {
      try {
        const data = JSON.parse(fs.readFileSync(verseFile, 'utf8'));
        verses.push({
          verse_number: i,
          data: data
        });
      } catch (err) {
        console.warn(`Error reading verse ${i}:`, err.message);
      }
    }
  }

  console.log(`Loaded ${verses.length} verses for Acts 10`);
  return verses;
};
