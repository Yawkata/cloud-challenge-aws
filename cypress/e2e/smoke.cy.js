describe('Frontend Smoke Test: Visitor Counter Integration', () => {
  it('loads the homepage and displays a valid visitor count from the API', () => {
    cy.visit('/')

    cy.get('#visitor-count')
      .should('exist')
      .invoke('text')
      .then((text) => {
        const count = Number(text)

        expect(text).to.not.be.empty
        expect(Number.isNaN(count)).to.be.false
        expect(count).to.be.at.least(0)
      })
  })
})
