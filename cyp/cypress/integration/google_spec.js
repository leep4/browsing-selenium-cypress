describe('Test Search', () => {
  it('Visits Google', () => {
    cy.visit('https://google.com')
    cy.get("[name='q']").type('casaba')
    cy.contains('Google Search').click()
    
    cy.get("[class='yuRUbf']").then(results => {
      for (let i = 0; i < results.length; i++) {
        const txt = results.eq(i).text()
        cy.log(txt)
      }
    })
  })
})