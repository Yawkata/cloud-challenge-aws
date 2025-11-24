const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',

    supportFile: false,
    
    baseUrl: process.env.CYPRESS_BASE_URL, 
    
    setupNodeEvents(on, config) {
    },
  },
})