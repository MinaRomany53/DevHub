/* Styling Project Form */
const titleEl = document.getElementById("id_title");
if (titleEl) titleEl.classList.add("input");

const imageEl = document.getElementById("id_image");
if (imageEl) imageEl.classList.add("input");

const imageClearEl = document.getElementById("image-clear_id");
if (imageClearEl) imageEl.classList.add("input");

const demoLinkEl = document.getElementById("id_demo_link");
if (demoLinkEl) demoLinkEl.classList.add("input");

const sourceLinkEl = document.getElementById("id_source_link");
if (sourceLinkEl) sourceLinkEl.classList.add("input");

const textareaEl = document.getElementById("id_description");
if (textareaEl) {
  textareaEl.classList.add("input");
  textareaEl.classList.add("input--textarea");
}

/*
 *
 *
 *
 */

/* Styling Profile Form */
const nameEl = document.getElementById("id_name");
if (nameEl) nameEl.classList.add("input");

const emailEL = document.getElementById("id_email");
if (emailEL) emailEL.classList.add("input");

const usernameEl = document.getElementById("id_username");
if (usernameEl) usernameEl.classList.add("input");

const headlineEl = document.getElementById("id_headline");
if (headlineEl) headlineEl.classList.add("input");

const locationEl = document.getElementById("id_location");
if (locationEl) locationEl.classList.add("input");

const socialGithubEl = document.getElementById("id_social_github");
if (socialGithubEl) socialGithubEl.classList.add("input");

const socialTwitter = document.getElementById("id_social_twitter");
if (socialTwitter) socialTwitter.classList.add("input");

const socialLinkedinEl = document.getElementById("id_social_linkedin");
if (socialLinkedinEl) socialLinkedinEl.classList.add("input");

const socialStackoverflowEl = document.getElementById(
  "id_social_stackoverflow"
);
if (socialStackoverflowEl) socialStackoverflowEl.classList.add("input");

const socialWebsite = document.getElementById("id_social_website");
if (socialWebsite) socialWebsite.classList.add("input");

const bioEl = document.getElementById("id_bio");
if (bioEl) {
  bioEl.classList.add("input");
  bioEl.classList.add("input--textarea");
}
