const path = require('path');

module.exports = function(eleventyConfig) {
  // Don't need to copy data directory as it's read at build time by _data files

  // Set input/output directories
  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data"
    }
  };
};
