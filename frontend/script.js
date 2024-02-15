// Function to handle sign up form submission
const signUpForm = document.querySelector('#signUpForm');
signUpForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(signUpForm);

    try {
        // Send POST request to backend API endpoint for sign up
        const response = await fetch('https://quicksearchestates.github.io/api/signup', {
            method: 'POST',
            body: formData
        });

        // Check if request was successful
        if (response.ok) {
            // Redirect user to dashboard or another page upon successful sign up
            window.location.href = 'https://quicksearchestates.github.io/dashboard';
        } else {
            // Display error message if sign up failed
            const errorMessage = await response.text();
            alert(errorMessage);
        }
    } catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('Error:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
});

// Function to handle property search form submission
const propertySearchForm = document.querySelector('#propertySearchForm');
propertySearchForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(propertySearchForm);

    try {
        // Send POST request to backend API endpoint for property search
        const response = await fetch('https://quicksearchestates.github.io/api/properties/search', {
            method: 'POST',
            body: formData
        });

        // Check if request was successful
        if (response.ok) {
            // Parse response JSON
            const properties = await response.json();

            // Display search results on the page (e.g., populate a list with property details)
            displaySearchResults(properties);
        } else {
            // Display error message if property search failed
            const errorMessage = await response.text();
            alert(errorMessage);
        }
    } catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('Error:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
});

// Function to display search results on the page
function displaySearchResults(properties) {
    // Implement logic to display search results (e.g., populate a list with property details)
    console.log(properties);
}

