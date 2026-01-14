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

  it('handles unexpected request payload safely', () => {
    cy.request({
      method: 'POST',
      url: Cypress.env('API_URL'),
      body: {
        foo: 'bar',
        random: 123,
      }
    })
      .then((response) => {
        expect(response.status).to.eq(200)
        expect(response.body).to.have.property('visitor_count')
        expect(response.body.visitor_count).to.be.a('number')
      })
  })

});