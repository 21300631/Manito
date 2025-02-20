function bringToFront(element) {
    let cards = Array.from(document.querySelectorAll('.card')); // Convertimos NodeList en Array
    let selectedIndex = cards.indexOf(element); // Encontramos el índice de la tarjeta seleccionada

    // Reorganizar las tarjetas en el nuevo orden
    let newOrder = [
        ...cards.slice(selectedIndex + 1), // Tarjetas después de la seleccionada
        ...cards.slice(0, selectedIndex),  // Tarjetas antes de la seleccionada
        element // La tarjeta seleccionada va al final (al frente)
    ];

    // Aplicar nuevos valores de posición y z-index
    newOrder.forEach((card, index) => {
        card.style.left = `${index * 40}px`; // Reposiciona cada tarjeta
        card.style.zIndex = index + 1; // Asigna un nuevo z-index en orden
    });
}
