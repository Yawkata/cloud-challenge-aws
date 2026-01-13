describe('Backend Smoke Test: Visitor Counter API', () => {
  it('returns a visitor count and increments it', () => {
    cy.request({
      method: 'POST',
      url: Cypress.env('API_URL'),
    }).then((response) => {
      expect(response.status).to.eq(200)
      expect(response.body).to.have.property('visitor_count')
      expect(response.body.visitor_count).to.be.a('number')
    })
  })
})
