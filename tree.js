async function insertKey() {
    const key = document.getElementById("key").value;
    const response = await fetch('http://127.0.0.1:5000/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: parseInt(key) })
    });

    if (response.ok) {
        drawTree();
    }
}

async function drawTree() {
    const response = await fetch('http://127.0.0.1:5000/get_tree');
    const data = await response.json();
    
    // Aqui você implementa a lógica para desenhar a árvore usando D3.js
    // Este código depende de como você quer visualizar os dados e pode ser complexo.
}

drawTree();  // Desenha a árvore quando a página carrega
