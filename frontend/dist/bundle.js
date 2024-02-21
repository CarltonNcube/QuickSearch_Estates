document.getElementById("signUpForm").addEventListener("submit",(async function(e){e.preventDefault();const t=document.getElementById("username").value,r=document.getElementById("email").value,o=document.getElementById("password").value;await async function(e,t,r){try{const o=await fetch("/api/signup",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({username:e,email:t,password:r})});if(o.ok){const e=await o.json();return console.log("User signed up successfully:",e),e}{const e=await o.text();throw new Error(e)}}catch(e){throw console.error("Error signing up:",e.message),e}}(t,r,o)})),document.getElementById("listPropertyForm").addEventListener("submit",(async function(e){e.preventDefault();const t=new FormData(this);await async function(e){try{const t=await fetch("/api/properties/list",{method:"POST",body:e});if(!t.ok)throw new Error("Failed to list property. Please try again.");const r=await t.json();console.log("Property listed successfully:",r)}catch(e){console.error("Error listing property:",e.message)}}(t)})),document.getElementById("propertySearchForm").addEventListener("submit",(async function(e){e.preventDefault(),await async function(e){try{const e=await fetch("/api/properties/search",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({})});if(!e.ok)throw new Error("Failed to search properties. Please try again.");const t=await e.json();displaySearchResults(t),displayPropertiesOnMap(t)}catch(e){console.error("Error searching properties:",e.message)}}()})),document.getElementById("saveFavoriteBtn").addEventListener("click",(async function(e){e.preventDefault(),await async function(e,t){try{if(!(await fetch("/api/users/user123/favorites",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({propertyId:"property456"})})).ok)throw new Error("Failed to save property as favorite. Please try again.");console.log("Property saved as favorite successfully.")}catch(e){console.error("Error saving property as favorite:",e.message)}}()}));
//# sourceMappingURL=bundle.js.map