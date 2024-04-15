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
    
    // Limpando o SVG para nova renderização
    d3.select("svg").selectAll("*").remove();

    // Configuração do layout da árvore
    const treeLayout = d3.tree().size([400, 400]);
    const root = d3.hierarchy(data);

    // Layout da árvore
    const treeData = treeLayout(root);

    // Desenho dos links (conexões)
    const links = d3.select("svg")
                    .selectAll(".link")
                    .data(treeData.links())
                    .enter()
                    .append("path")
                    .classed("link", true)
                    .attr("d", d3.linkVertical()
                        .x(d => d.x + 480)  // Centralizando horizontalmente
                        .y(d => d.y + 50)); // Deslocamento vertical

    // Desenho dos nós
    const nodes = d3.select("svg")
                    .selectAll(".node")
                    .data(treeData.descendants())
                    .enter()
                    .append("g")
                    .attr("class", "node")
                    .attr("transform", d => `translate(${d.x + 480},${d.y + 50})`);

    nodes.append("circle")
         .attr("r", 10);

    nodes.append("text")
         .attr("dy", "0.35em")
         .attr("y", d => d.children ? -20 : 20)
         .style("text-anchor", "middle")
         .text(d => d.data.key);
}

drawTree();  // Desenha a árvore quando a página carrega
