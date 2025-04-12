describe('Navigation', () => {
    it('Navigates to the products page', () => {
      cy.visit('http://localhost:3000/');
      cy.get('nav a[href="/products"]').click();
      cy.url().should('include', '/products');
      cy.contains('Products List'); // Verifica que la página tiene un título
    });
  });