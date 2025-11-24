describe('Smoke Test: Homepage Health Check', () => {
  it('should load the homepage and display the main title', () => {
    cy.visit('/') 
    cy.get('body').should('be.visible'); 
  })
})