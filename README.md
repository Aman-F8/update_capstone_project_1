# Project Summary

This mini-project automates testing of the [GUVI](https://www.guvi.in) website using **Python**, **Selenium**, and **Pytest**. It covers end-to-end functionality checks such as validating the website URL and title, verifying visibility and clickability of login and signup buttons, navigating to the sign-in page, and performing both valid and invalid login tests. The automation suite includes both **positive and negative scenarios**, structured with Pytest for ease of execution and maintainability. The project generates HTML reports and uses best practices like Page Object Model and explicit waits.


# MINI-PROJECT-01: Web Automation Using Python Selenium and Pytest

**Title:**  
Automating the Web Application [GUVI](https://www.guvi.in) using Python Selenium and Pytest Framework.

---

## Test Objective

The goal of this project is to **automate the GUVI web application** using the **Python Selenium framework** along with **Pytest** for structuring and executing the test cases. 
This automation will include **positive and negative scenarios** across different web elements and actions.

---

## Tools Used

- **Python**
- **Selenium WebDriver**
- **Pytest**

---

## Target URL

> [https://www.guvi.in](https://www.guvi.in)

---

## Precondition

Test cases include **all positive and negative scenarios** for the provided test objectives.

---

## Test Suite

### **Test Case 1:** Validate URL  
- Verify that the URL `https://www.guvi.in` is valid and accessible.

### **Test Case 2:** Page Title Validation  
- Verify that the webpage title is:  
  **"GUVI | Learn the code in your native language"**

### **Test Case 3:** Login Button Test  
- Check whether the **Login** button is visible.  
- Verify that the **Login** button is clickable.

### **Test Case 4:** Sign-up Button Test  
- Check whether the **Sign-up** button is visible.  
- Verify that the **Sign-up** button is clickable.

### **Test Case 5:** Navigate to Sign-in Page  
- Click the **Sign-up** button and ensure redirection to `https://www.guvi.in/sign-in/`.  
- Verify that the sign-in page loads correctly.

### **Test Case 6:** Valid Login and Logout Test  
- Login to your GUVI account using **valid email and password**.  
- Verify successful login (e.g., by checking cookies or page content).  
- Logout from your account and verify logout functionality.

### **Test Case 7:** Invalid Login Test  
- Attempt login with **invalid email and password**.  
- Capture and verify the **error message** shown on failed login.

---


