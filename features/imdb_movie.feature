Feature: Consultar una película en IMDb y comprobar su puntuación
Scenario: Confirmar que al buscar "Inception" se muestra el título y la calificación correctos
Given la persona usuaria ingresa a la página principal de IMDb
When introduce la película "Inception" en el buscador
And accede al primer resultado mostrado
Then el título mostrado para la película debe ser "Inception"
And la puntuación de la película debe aparecer visible