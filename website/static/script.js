// const currentDate = new Date();

// function getWeekRange(date) {
//     const day = date.getDay();
//     const startDate = new Date(date);
//     startDate.setDate(date.getDate() + (day === 6 ? 0 : 0));
    
//     const endDate = new Date(startDate);
//     endDate.setDate(startDate.getDate() + (6 - startDate.getDay())); // Set to next Saturday

//     return [startDate, endDate];
// }

// function updateCalendar() {
//     const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
//     const month = currentDate.getMonth();
//     const year = currentDate.getFullYear();

//     document.getElementById('calendar-month').textContent = monthNames[month];
//     document.getElementById('calendar-year').textContent = year;

//     const firstDayOfMonth = new Date(year, month, 1);
//     const lastDayOfMonth = new Date(year, month + 1, 0);
//     const daysInMonth = lastDayOfMonth.getDate();

//     const calendarDays = document.getElementById('calendar-days');
//     calendarDays.innerHTML = ''; 

//     for (let i = 0; i < firstDayOfMonth.getDay(); i++) {
//         const emptyDay = document.createElement('div');
//         emptyDay.className = 'calendar__day empty';
//         calendarDays.appendChild(emptyDay);
//     }

//     for (let i = 1; i <= daysInMonth; i++) {
//         const dayElement = document.createElement('div');
//         dayElement.className = 'calendar__day';
//         dayElement.textContent = i;
//         calendarDays.appendChild(dayElement);
//     }
//     highlightCurrentWeek();
// }

// function highlightCurrentWeek() {
//     const [startDate, endDate] = getWeekRange(currentDate);
//     const weekDays = document.querySelectorAll('.calendar__day');
//     const today = currentDate.getDate();

//     console.log("Start Date of Week:", startDate);
//     console.log("End Date of Week:", endDate);

//     weekDays.forEach(day => {
//         const dayNumber = parseInt(day.textContent, 10);

//         if (!isNaN(dayNumber)) {
//             const dayDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), dayNumber);

//             if (dayDate.toDateString() === currentDate.toDateString()) {
//                 day.style.backgroundColor = '#f19b0e';
//                 day.style.color = 'white';
//             } else if (dayDate >= startDate && dayDate <= endDate && dayDate > currentDate) {
//                 day.style.backgroundColor = '#c07a0a';
//                 day.style.color = 'white';
//             }
//             console.log("Processing Day:", dayNumber, "Date:", dayDate);
//         }
//     });
// }

// function updateWeekView(startDate) {
//     const weekDays = document.querySelectorAll('.day');
//     const weekRange = getWeekRange(startDate);

//     weekDays.forEach((dayElement, index) => {
//         const currentDate = new Date(weekRange[0]);
//         currentDate.setDate(currentDate.getDate() + index);
//         dayElement.textContent = currentDate.toLocaleString('en-us', { weekday: 'long' });
//     });
// }

// window.onload = updateCalendar;


// CODE FOR ALL PAGES
// Function that runs all functions that are necessary on all pages
function runAllFunctions(companion) {
    expectModalClick();
    setNavLinkActive();
    showCorrectCompanionIcon(companion);
    if (user_logged_in && bad_habit === 0) {
        launchBriefQuestionnaire();
    }
}

// Toggle dropdown menu
function toggleMenu() {
    const menu = document.getElementById("sub-menu-container");
    menu.classList.toggle("open-menu");
}

// dropdown menu - show and hide
document.addEventListener("DOMContentLoaded", () => {
    const menu = document.getElementById("sub-menu-container");
    const profileIcon = document.querySelector(".profile-icon");

    document.addEventListener("click", function (event) {
        if (menu && profileIcon) {
            if (!menu.contains(event.target) && !profileIcon.contains(event.target)) {
                menu.classList.remove("open-menu");
            }
        }
    });

    window.addEventListener("scroll", function () {
        if (menu && menu.classList.contains("open-menu")) {
            menu.classList.remove("open-menu");
        }
    });
});

// display correct companion in navigation bar
function showCorrectCompanionIcon(companion) {
    const companionImages = {
        "dog": "dog.png",
        "plant": "plant.jpg",
        "slime": "slime.png",
        "cat": "cat.jpg",
        "dragon": "dragon.png",
    };

    const imageFilename = companionImages[companion] || "user-icon.png"; // Default image if companion not found

    const companionImage = document.getElementById('companion-image');
    if (companionImage) {
        companionImage.src = "static/images/" + imageFilename;
    }
}

// Navbar animation code
const navbar = document.querySelector('.navbar');
let lastScrollTop = 0;

window.addEventListener('scroll', function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    // if we're at the top of the page (scroll position 0)
    if (currentScroll <= 0) {
        navbar.classList.remove('slide-up');
        navbar.classList.add('slide-down');
    } 
    // if scrolling down
    else if (currentScroll > lastScrollTop) {
        navbar.classList.remove('slide-down');
        navbar.classList.add('slide-up');
    } 
    // if scrolling up
    else {
        navbar.classList.remove('slide-up');
        navbar.classList.add('slide-down');
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});

// Set active navigation link in navbar if the user is on that page
function setNavLinkActive() {
    const pageMap = {
        "/Index": "home-link",
        "/About": "about-link",
        "/Contact": "contact-link",
        "/Settings": "settings-link",
        "/Companion-hub": "companion-hub-link",
    };
    const currentPath = window.location.pathname;
    const activeLinkId = pageMap[currentPath];

    if (activeLinkId) {
        const activeLink = document.getElementById(activeLinkId);
        if (activeLink) {
            activeLink.classList.add("nav-link-active");
        }
    }
}

// Slider code
function showSlider() {
    const sliderContainer1 = document.getElementById("slider-container-1");
    const sliderContainer2 = document.getElementById("slider-container-2");
  
    const squareData = [
      { type: "color", value: "var(--neutral-foam)" },
      { type: "color", value: "var(--neutral-pink)" },
      { type: "color", value: "var(--neutral-cinderella)" },
      { type: "color", value: "var(--neutral-foam)" },
      { type: "image", value: "dog.png" },
      { type: "color", value: "var(--neutral-pink)" },
      { type: "image", value: "dragon.png" },
      { type: "color", value: "var(--neutral-cinderella)" },
      { type: "color", value: "var(--neutral-pink)" },
      { type: "image", value: "cat.jpg" },
      { type: "image", value: "slime.png" },
      { type: "color", value: "var(--neutral-cinderella)" },
      { type: "color", value: "var(--neutral-foam)" },
      { type: "image", value: "plant.jpg" },
    ];
  
    const totalSquares = 50;
    const extendedArray = [];
    for (let i = 0; i < totalSquares; i++) {
      extendedArray.push(squareData[i % squareData.length]);
    }
  
    extendedArray.forEach((data) => {
      const square = createSquare(data);
      sliderContainer1.appendChild(square);
    });
  
    extendedArray.reverse().forEach((data) => {
      const square = createSquare(data);
      sliderContainer2.appendChild(square);
    });
  
    sliderContainer1.classList.add("animated");
    sliderContainer2.classList.add("animated-reverse");
  }
  
  function createSquare(data) {
    const square = document.createElement("div");
    square.classList.add("square");
  
    if (data.type === "color") {
      square.style.backgroundColor = data.value;
    } else if (data.type === "image") {
      const img = document.createElement("img");
      img.src = "static/images/" + data.value;
      img.classList.add("square-img");
      square.appendChild(img);
    }
  
    return square;
}
  

// Toggle for password visibility
const passwordFields = [
    { toggle: document.getElementById("toggle-password-sign-in"), input: document.getElementById("password-sign-in")},
    { toggle: document.getElementById("toggle-registration-password"), input: document.getElementById("registration-password") },
    { toggle: document.getElementById("toggle-confirm-password"), input: document.getElementById("confirm-password") }
];

const passwordInput1 = document.getElementById("registration-password");
const confirmPasswordContainer = document.getElementById("confirm-password-container");
const passwordMismatchError = document.getElementById("password-mismatch-error");

function togglePasswordVisibility() {
    passwordFields.forEach(field => {
        field.toggle.addEventListener("click", () => {
            const isPasswordVisible = field.input.getAttribute("type") === "text";
            field.input.setAttribute("type", isPasswordVisible ? "password" : "text");

            field.toggle.src = isPasswordVisible
                ? "static/images/eye-hide.png"
                : "static/images/eye-view.png";
        });
    });
}

// Modals / Popups code
const modals = [
    { modal: document.getElementById("sign-in-modal"), link: document.querySelectorAll("#sign-in-link"), close: document.getElementById("close-btn-1")},
    { modal: document.getElementById("registration-modal"), link: document.querySelectorAll("#registration-link"), close: document.getElementById("close-btn-2")},
];

function expectModalClick() {
    modals.forEach(({modal, link, close}) => {
        if (link instanceof NodeList) {
            link.forEach(button => {
                button.addEventListener("click", function(event) {
                    event.preventDefault();
                    modal.style.display = "block"; 

                    document.body.classList.add('stopScroll');

                    modals.forEach(({modal: otherModal}) => {
                        if (otherModal !== modal) {
                            otherModal.style.display = "none";
                        }
                    });
                });
            });
        } else {
            link.addEventListener("click", function(event) {
                event.preventDefault();
                modal.style.display = "block";

                document.body.classList.add('stopScroll');
                
                modals.forEach(({modal: otherModal}) => {
                    if (otherModal !== modal) {
                        otherModal.style.display = "none";
                    }
                });
            });
        }

        close.addEventListener("click", function() {
            modal.style.display = "none";
            document.body.classList.remove('stopScroll');
        })
    });

    window.addEventListener("click", function(event) {
        modals.forEach(({modal}) => {
            if(event.target === modal) {
                modal.style.display = "none";
                document.body.classList.remove('stopScroll');
            }
        });
    });

    togglePasswordVisibility();

    // hide & show confirm_password field
    passwordInput1.addEventListener("blur", function() {
        if (passwordInput1.value.trim() !== "") {
            confirmPasswordContainer.classList.add("show");
        }
    });

    // Check if passwords match confirm_password before form submission
    document.getElementById("registration-form").addEventListener("submit", function(event) {
        const password = document.getElementById("registration-password").value;
        const confirmPassword = document.getElementById("confirm-password").value;
        
        document.getElementById("registration-password").classList.remove("error");
        document.getElementById("confirm-password").classList.remove("error");
        passwordMismatchError.style.display = "none"; 

        if (password !== confirmPassword) {
            event.preventDefault();
            passwordMismatchError.style.display = "flex";
            document.getElementById("confirm-password").classList.add("error"); 
            document.getElementById("registration-password").classList.add("error");
        }
    });
}

// Brief Questionnaire code to show multiple pages
function launchBriefQuestionnaire() {
    const briefQuestionnaireModal = document.getElementById('brief-questionnaire-modal')
    const pages = document.querySelectorAll('.questionnaire-page');

    briefQuestionnaireModal.style.display = 'block';
    document.body.classList.add('stopScroll');
    
    showPage(0);

    function showPage(pageIndex) {
        pages.forEach((page, index) => page.style.display = index === pageIndex ? 'block' : 'none');
    }

    // event listener for navigation buttons (next/previous)
    document.querySelectorAll('.navigate-button').forEach(button => {
        button.addEventListener('click', (e) => {
        const currentPageIndex = parseInt(button.getAttribute('data-current-page'));
        const direction = button.getAttribute('data-direction');
        const newPageIndex = direction === 'next' ? currentPageIndex + 1 : currentPageIndex - 1;
    
        if (newPageIndex >= 0 && newPageIndex < pages.length) {
            if (direction === 'next') {
            if (isValidPage(currentPageIndex)) { showPage(newPageIndex);
            } else { e.preventDefault(); }
            } else { showPage(newPageIndex); }
        }
        });
    });

    // event listener for submit button
    document.getElementById('submit-questionnaire').addEventListener('click', (e) => {
        if (!isValidPage(pages.length - 1)) { 
            e.preventDefault(); 
        } else {
            document.getElementById('questionnaire-form').submit();
            document.body.classList.remove('stopScroll');
            briefQuestionnaireModal.style.display = 'none';
        }
    });

    // Prevent the form from resetting when going to next or previous page
    document.getElementById('questionnaire-form').addEventListener('submit', (e) => {
        e.preventDefault();
    });
}

// validate inputs
function isValidPage(pageIndex) {
    let isValid = true;
  
    // page 1
    if (pageIndex === 0) {
      const waiverCheckbox = document.getElementById('questionnaire-waiver');
      const waiverError = document.getElementById('waiver-error');
      if (!waiverCheckbox.checked) {
        waiverError.style.display = 'block';
        isValid = false;
      } else {
        waiverError.style.display = 'none';
      }
    }
  
    // page 2
    if (pageIndex === 1) {
      const badHabitInput = document.getElementById('bad-habit');
      const goalDurationSelect = document.getElementById('goal-duration');
      const companionNameInput = document.getElementById('companion-name');
      const badHabitError = document.getElementById('bad-habit-error');
      const goalDurationError = document.getElementById('goal-duration-error');
      const companionNameError = document.getElementById('companion-name-error');
  
      if (!badHabitInput.value.trim()) {
        badHabitError.style.display = 'block';
        isValid = false;
      } else {
        badHabitError.style.display = 'none';
      }
  
      if (goalDurationSelect.value == "default") {
        goalDurationError.style.display = 'block';
        isValid = false;
      } else {
        goalDurationError.style.display = 'none';
      }
    }

    // Page 3
    if (pageIndex === 2) {
        const companionNameInput = document.getElementById('companion-name');
        const companionRadio = document.querySelectorAll('input[name="companion"]');
        const companionError = document.getElementById('companion-error');
        const companionNameError = document.getElementById('companion-name-error');
        let companionSelected = false;

        if (!companionNameInput.value.trim()) {
          companionNameError.style.display = 'block';
          isValid = false;
        } else {
          companionNameError.style.display = 'none';
        }

        companionRadio.forEach(radio => {
            if (radio.checked) {
                companionSelected = true;
            }
        });
    
        if (!companionSelected) {
            companionError.style.display = 'block';
            isValid = false;
            companionRadio[0].focus();
        } else {
            companionError.style.display = 'none';
        }
    }
  
    return isValid;
}

// CODE FOR HOME PAGE

// Testimony slideshow code on home page
// Placeholders for now, since we do not have any real feedback and are not storing them in database
const testimonials = [
    {
        avatar: "static/images/dog.png",
        name: "Cara Lopez",
        title: "AMAZING WEB APP!",
        rating: "⭐⭐⭐⭐⭐",
        text: "Energy drinks used to control my life — I struggled for years to cut back, trying every method I could find, but nothing really worked. Then I found HabiTrain, and it made all the difference. It gave me the motivation I desperately needed, and honestly, it was so rewarding to see my little puppy grow as I made progress. Breaking this bad habit finally felt doable — and even fun. Thank you, HabiTrain!"
    },
    {
        avatar: "static/images/plant.jpg",
        name: "Alex Martin",
        title: "Quit for Good!",
        rating: "⭐⭐⭐⭐⭐",
        text: "Quitting smoking felt impossible - until HabiTrain came into my life. The way it tracked my progress and kept me motivated at every turn was a game changer. Each small win built up my confidence, and now, for the first time in years, I feel free. I can’t thank HabiTrain enough for giving me my life back.",
    },
    {
        avatar: "static/images/dog.png",
        name: "Sofia Nguyen",
        title: "A life-changer!",
        rating: "⭐⭐⭐⭐⭐",
        text: "I used to waste hours endlessly scrolling on my phone — it was draining and unproductive. HabiTrain helped me break free from that cycle with its simple steps and progress tracking. Seeing how much time I regained every day was incredibly motivating, and now, I spend my time doing what really matters. Whether it's focusing on my hobbies or spending quality time with loved ones, I feel happier and more in control of my life.",
    },
    {
        avatar: "static/images/plant.jpg",
        name: "John Doe",
        title: "Changed My Life!",
        rating: "⭐⭐⭐⭐⭐",
        text: "Thanks to HabiTrain, I finally managed to break free from years of procrastination. It made building healthy habits so much easier, and the cute graphics kept me coming back every day! I loved how it made the journey feel rewarding, celebrating even small victories. Now, I'm achieving goals I thought I'd never reach — HabiTrain truly changed my life for the better!"
    },
];


function expectTestimoniesAction() {
    const avatar = document.getElementById("testimony-avatar");
    const author = document.getElementById("testimony-name");
    const title = document.getElementById("testimony-title");
    const text = document.getElementById("testimony-text");
    const bars = document.querySelectorAll("#testimony-bar");
    const card = document.getElementById("testimonial-card");

    let currentIndex = 0;
    let isAnimating = false;

    function updateTestimonialContent(index) {
        const testimonial = testimonials[index];
        avatar.src = testimonial.avatar;
        author.textContent = testimonial.name;
        title.innerHTML = `${testimonial.title} <span class="testimonial-rating">${testimonial.rating}</span>`;
        text.textContent = testimonial.text;

        bars.forEach((bar, idx) => {
            bar.classList.toggle("active", idx === index);
        });
    }

    function animateTestimonial(direction) {
        if (isAnimating) return;
        isAnimating = true;

        const outgoingClass = direction === "left" ? "slide-out-left" : "slide-out-right";
        card.classList.add(outgoingClass);

        card.addEventListener(
            "animationend",
            (event) => {
                if (event.animationName === "slide-out-left" || event.animationName === "slide-out-right") {
                    card.classList.remove(outgoingClass);
                    updateTestimonialContent(currentIndex);

                    const incomingClass = direction === "left" ? "slide-in-right" : "slide-in-left";
                    card.classList.add(incomingClass);

                    card.addEventListener(
                        "animationend",
                        (event) => {
                            if (event.animationName === "slide-in-left" || event.animationName === "slide-in-right") {
                                card.classList.remove(incomingClass);
                                isAnimating = false;
                            }
                        },
                        { once: true }
                    );
                }
            },
            { once: true }
        );
    }

    document.querySelector(".next-btn").addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % testimonials.length;
        animateTestimonial("left");
    });

    document.querySelector(".prev-btn").addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
        animateTestimonial("right");
    });

    bars.forEach((bar, idx) => {
        bar.addEventListener("click", () => {
            if (idx !== currentIndex) {
                const direction = idx > currentIndex ? "left" : "right";
                currentIndex = idx;
                animateTestimonial(direction);
            }
        });
    });

    updateTestimonialContent(currentIndex);
}

// CODE FOR SETTINGS PAGE

// Showing selected companion during view mode, blocking selection of others
function showSelectedCompanion(selectedCompanion) {
    const companionRadio = document.querySelector(`input[type="radio"][value="${selectedCompanion}"]`);
    if (companionRadio) {
        companionRadio.checked = true; 

        const allRadioButtons = document.querySelectorAll('input[type="radio"][name="companion"]');
        allRadioButtons.forEach(button => {
            button.disabled = true;
        });
    }
}

function showSelectedGoalDuration(goalDuration) {
    const goalSelect = document.getElementById("goal-duration");
    if (goalDuration && goalDuration !== "default") {
        goalSelect.value = goalDuration;
        goalSelect.disabled = true;
    }
}

// Showing edit mode
function setupSettingsForm(originalValues) {
    const editButton = document.getElementById("edit-button");
    const form = document.getElementById("settings-form");
    const inputs = form.querySelectorAll("input[readonly]");
    const select = form.querySelectorAll("select[readonly]")
    const radioButtons = form.querySelectorAll('input[type="radio"]');
    const hubButton = document.getElementById("hub-btn");
    const saveButton = document.getElementById("save-btn");
    const cancelButton = document.getElementById("cancel-btn");

    function enableEditMode() {
        inputs.forEach(input => input.removeAttribute("readonly"));
        select.forEach(button => (button.disabled = false))
        radioButtons.forEach(button => (button.disabled = false));

        saveButton.style.display = "block";
        cancelButton.style.display = "block";

        editButton.style.display = "none";
        hubButton.style.display = "none";
    }

    function cancelEditMode() {
        revertChanges(originalValues);

        inputs.forEach(input => input.setAttribute("readonly", true));
        select.forEach(button => (button.disabled = true))
        radioButtons.forEach(button => (button.disabled = true));

        saveButton.style.display = "none";
        cancelButton.style.display = "none";

        editButton.style.display = "inline-block";
        hubButton.style.display = "inline-block";        
    }

    editButton.addEventListener("click", enableEditMode);
    cancelButton.addEventListener("click", cancelEditMode);
    saveButton.addEventListener("click", () => {
        form.submit();
    })
}

function revertChanges(originalValues) {
    document.getElementById("username").value = originalValues.username;
    document.getElementById("email").value = originalValues.email;
    document.getElementById("bad_habit").value = originalValues.bad_habit;
    document.getElementById("companion-name").value = originalValues.companionName;

    showSelectedCompanion(originalValues.selectedCompanion);
    showSelectedGoalDuration(originalValues.goalDuration);
}

//Code for About us page
// Function to open the modal
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.style.display = "block"; // Show the modal
      document.body.style.overflow = "hidden"; // Prevent background scrolling
    }
  }
  
  // Function to close the modal
  function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.style.display = "none"; // Hide the modal
      document.body.style.overflow = ""; // Restore background scrolling
    }
  }
  
  // Add event listeners to close modals when clicking outside or on close button
  window.addEventListener("click", function (event) {
    const modals = document.querySelectorAll(".modal");
    modals.forEach((modal) => {
      if (event.target === modal) {
        modal.style.display = "none"; // Close modal if clicked outside content
        document.body.classList.remove("stopScroll");
      }
    });
  });