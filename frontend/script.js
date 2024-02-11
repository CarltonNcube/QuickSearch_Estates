// Function to handle sign up form submission
const signUpForm = document.querySelector('#signUpForm');
signUpForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(signUpForm);

    try {
        // Send POST request to backend API endpoint for sign up
        const response = await fetch('/api/signup', {
            method: 'POST',
            body: formData
        });

        // Check if request was successful
        if (response.ok) {
            // Redirect user to dashboard or another page upon successful sign up
            window.location.href = '/dashboard';
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
        const response = await fetch('/api/properties/search', {
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

// Function to fetch data from the backend API endpoint
function fetchData() {
    fetch('http://quicksearchestates.wuaze.com/api/data')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle data received from the backend
            console.log(data);
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
        });
}

// Call the fetchData function to initiate the request
fetchData();

