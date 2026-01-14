const path = require('path');

module.exports = function(eleventyConfig) {
  // Add custom filter to check if value is an array
  eleventyConfig.addFilter("isArray", function(value) {
    return Array.isArray(value);
  });

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
