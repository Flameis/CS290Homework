function searchText(searchTerm, pages) {
    let searchResults = [];

    pages.forEach(page => {
        const iframe = document.createElement("iframe");
        iframe.src = page;
        iframe.onload = () => {
            const iframeDoc = iframe.contentWindow.document;
            const pageText = iframeDoc.body.innerText.toLowerCase();
            const regex = new RegExp(searchTerm, "gi"); // Case-insensitive search
            
            // Highlight found text
            const highlightedText = pageText.replace(regex, match => `<span class="highlight">${match}</span>`);
            iframeDoc.body.innerHTML = highlightedText;

            // Check if the search term is found in the page
            if (pageText.includes(searchTerm)) {
                searchResults.push(page);
            }

            // Display search results
            displayResults(searchResults);
        };

        document.body.appendChild(iframe);
    });
}

function displayResults(results) {
    const searchResultsDiv = document.getElementById("searchResults");
    searchResultsDiv.innerHTML = "";

    if (results.length === 0) {
        searchResultsDiv.textContent = "No results found.";
    } else {
        const ul = document.createElement("ul");
        results.forEach(result => {
            const li = document.createElement("li");
            li.textContent = result;
            ul.appendChild(li);
        });
        searchResultsDiv.appendChild(ul);
    }
}