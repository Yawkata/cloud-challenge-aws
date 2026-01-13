describe('Backend Smoke Test: Visitor Counter API', () => {

  it('validates response structure and verifies counter increment', () => {
    cy.request('POST', Cypress.env('API_URL')).then((firstResponse) => {

      expect(firstResponse.status).to.eq(200, 'Initial request should be successful');
      expect(firstResponse.body).to.have.property('visitor_count');
      
      const firstCount = firstResponse.body.visitor_count;
      expect(firstCount).to.be.a('number');

      cy.request('POST', Cypress.env('API_URL')).then((secondResponse) => {
        
        const secondCount = secondResponse.body.visitor_count;
        expect(secondCount, 'The counter should increase by at least 1').to.be.greaterThan(firstCount);
      });
    });
  });
});