// Function to handle user authentication
async function signIn(email, password) {
    try {
        const response = await fetch('https://www.krismaholdings.tech/api/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const userData = await response.json();
            // Store user data in localStorage or session storage for session management
            // Example: localStorage.setItem('userData', JSON.stringify(userData));
            console.log('User signed in:', userData);
            return userData;
        } else {
            const errorMessage = await response.text();
            throw new Error(errorMessage);
        }
    } catch (error) {
        console.error('Error signing in:', error.message);
        throw error;
    }
}

// Function to handle property search
async function searchProperties(searchQuery) {
    try {
        const formData = new FormData();
        formData.append('searchQuery', searchQuery);

        const response = await fetch('https://www.krismaholdings.tech/api/properties/search', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to search properties. Please try again.');
        }

        const properties = await response.json();
        displaySearchResults(properties);
        displayPropertiesOnMap(properties);
    } catch (error) {
        console.error('Error searching properties:', error.message);
    }
}

// Function to display search results on the page
function displaySearchResults(properties) {
    const propertyList = document.getElementById('propertyList');
    propertyList.innerHTML = ''; // Clear previous results

    properties.forEach(property => {
        const listItem = document.createElement('li');
        listItem.textContent = property.address;
        propertyList.appendChild(listItem);
    });
}

// Function to display properties on a map using Leaflet
function displayPropertiesOnMap(properties) {
    const map = L.map('map').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    properties.forEach(property => {
        L.marker([property.latitude, property.longitude]).addTo(map)
            .bindPopup(property.address)
            .openPopup();
    });
}

// Event listener for property search form submission
document.getElementById('propertySearchForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission behavior
    const searchAddress = document.getElementById('searchAddress').value;
    await searchProperties(searchAddress);
});

// Simulated form data
const signUpFormData = new FormData();
signUpFormData.append('email', 'test@example.com');
signUpFormData.append('password', 'password123');

// Simulate form submission
submitSignUpForm(signUpFormData);

// Simulated property search form data
const propertySearchFormData = new FormData();
propertySearchFormData.append('searchQuery', 'house');

// Simulate property search
searchProperties(propertySearchFormData);

