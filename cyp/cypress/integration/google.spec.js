const SRCH_STR = 'casaba'

describe('Test Search', () => {
  it('Visits Google', () => {
    cy.visit('https://google.com')
    cy.get("[name='q']").type(SRCH_STR)
    cy.contains('Google Search').click()
    
    cy.get("[class='yuRUbf']").then(results => {
      for (let i = 0; i < results.length; i++) {
        const name = results.eq(i).find('h3').text()
        const url = results.eq(i).find('a').attr('href')
        cy.log(name, url)
      }
    })
  })
})