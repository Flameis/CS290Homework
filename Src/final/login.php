<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Define the expected password
    $expectedPassword = "your_password_here";

    // Retrieve the entered password from the form
    $enteredPassword = $_POST["password"];

    // Perform password validation
    if ($enteredPassword === $expectedPassword) {
        // Password is correct, redirect to the mutators page
        header("Location: mutators.php");
        exit;
    } else {
        // Password is incorrect, display an error message
        $errorMessage = "Incorrect password. Please try again.";
    }
}
?>