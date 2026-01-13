Feature: Ver pagina para hacer Inicio de sesión
    Como usuario registrado
    Quiero diligenciar el formulario de ingreso para poder acceder a la plaataforma

    Background:
        Given que estoy en la página de Login
    
Scenario: Inicio de sesión exitoso
        When el usuario ingresa el nombre de usuario "Admin"
        And el usuario ingresa la contraseña "admin123"
        And el usuario hace clic en el botón "Login"
        Then el sistema debe redirigirlo a la página de "Dashboard"
        And el encabezado de la página debe mostrar el texto "Dashboard"

Scenario: Inicio de sesión no exitoso
        When el usuario ingresa el nombre de usuario "123456789"
        And el usuario ingresa la contraseña "123456789"
        And el usuario hace clic en el botón "Login"
        Then el sistema debe mostrar un mensaje de error "Invalid credentials"
        And los campos de "Username" y "Password" deben seguir visibles

Scenario: Intento de inicio de sesión con campos vacíos
        When el usuario deja el campo de nombre de usuario vacío
        And el usuario deja el campo de contraseña vacío
        And el usuario hace clic en el botón "Login"
        Then el sistema debe mostrar el mensaje "Required" en ambos campos
        And el usuario debe permanecer en la página de inicio de sesión