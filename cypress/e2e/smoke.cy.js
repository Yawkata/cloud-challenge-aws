describe('Frontend Smoke Test: Visitor Counter Integration', () => {
  it('loads the homepage and displays a valid visitor count from the API', () => {
    let firstCount

    cy.visit('/')

    cy.get('#visitor-count')
      .should('exist')
      .invoke('text')
      .then((text) => {
        firstCount = Number(text)

        expect(text).to.not.be.empty
        expect(Number.isNaN(firstCount)).to.be.false
        expect(firstCount).to.be.at.least(0)
      })

    cy.reload()

    cy.get('#visitor-count')
      .invoke('text')
      .then((text) => {
        const secondCount = Number(text)

        expect(Number.isNaN(secondCount)).to.be.false
        expect(secondCount).to.eq(firstCount)
      })
  })
})
