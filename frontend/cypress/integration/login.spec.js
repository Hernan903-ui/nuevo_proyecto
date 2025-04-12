describe('Login Form', () => {
    it('Logs in successfully', () => {
      cy.visit('http://localhost:3000/login'); // Cambia la URL si es necesario
      cy.get('input[name="email"]').type('test@example.com');
      cy.get('input[name="password"]').type('password123');
      cy.get('button[type="submit"]').click();
      cy.url().should('include', '/dashboard'); // Verifica que redirige al dashboard
    });
  
    it('Shows error for invalid credentials', () => {
      cy.visit('http://localhost:3000/login');
      cy.get('input[name="email"]').type('invalid@example.com');
      cy.get('input[name="password"]').type('wrongpassword');
      cy.get('button[type="submit"]').click();
      cy.get('.error-message').should('be.visible'); // Verifica que aparece un mensaje de error
    });
  });