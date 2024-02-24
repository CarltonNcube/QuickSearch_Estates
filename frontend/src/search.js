// search.js

document.getElementById('searchForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const minPrice = document.getElementById('minPrice').value;
    const maxPrice = document.getElementById('maxPrice').value;
    const propertyType = document.getElementById('propertyType').value;

    const queryParams = new URLSearchParams({
        location,
        minPrice,
        maxPrice,
        propertyType
    });

    try {
        const response = await fetch(`/api/properties/search?${queryParams}`);

        if (response.ok) {
            const data = await response.json();
            displaySearchResults(data);
        } else {
            console.error('Search failed');
            // Display error message to the user
        }
    } catch (error) {
        console.error('Error searching:', error.message);
    }
});

function displaySearchResults(results) {
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = '';

    if (results.length === 0) {
        searchResultsDiv.textContent = 'No results found';
        return;
    }

    results.forEach(result => {
        // Create a container for each property
        const propertyContainer = document.createElement('div');
        propertyContainer.classList.add('property-container');

        // Create image element for property
        const propertyImage = document.createElement('img');
        propertyImage.src = result.imageURL; // Assuming imageURL is a property of the search result object
        propertyImage.alt = result.propertyName; // Assuming propertyName is a property of the search result object
        propertyImage.classList.add('property-image');

        // Add click event listener to property image
        propertyImage.addEventListener('click', function() {
            // Redirect user to property details page
            window.location.href = `/property-details.html?id=${result.id}`;
        });

        // Append image to property container
        propertyContainer.appendChild(propertyImage);

        // Create other elements for property details (e.g., property name, price, etc.)
        // Append these elements to the property container

        // Append property container to search results div
        searchResultsDiv.appendChild(propertyContainer);
    });
}

