/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    "!../../**/node_modules",
    /* JS 2: Process all JavaScript files in the project. */
    "../../**/*.js",
    "../../**/react/**/*.jsx",

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      colors: {
        primary: "#26282a",
        secondary: "#090809",
        accent: "#e40712",
        "primary-fg": "#fff",
        "body-fg": "#333",
        "body-bg": "#fff",
        "body-quiet-color": "#666",
        "body-loud-color": "#000",
        "header-color": "#fff",
        "header-branding-color": "var(--accent)",
        "header-bg": "var(--secondary)",
        "header-link-color": "var(--primary-fg)",
        "breadcrumbs-fg": "#a5afba",
        "breadcrumbs-link-fg": "var(--body-bg)",
        "breadcrumbs-bg": "var(--primary)",
        "link-fg": "#bc0f0f",
        "link-hover-color": "#e40712",
        "link-selected-fg": "#5b80b2",
        "hairline-color": "#e8e8e8",
        "border-color": "#ccc",
        "error-fg": "#ba2121",
        "message-success-bg": "#dfd",
        "message-warning-bg": "#ffc",
        "message-error-bg": "#ffefef",
        "darkened-bg": "#f8f8f8",
        "selected-bg": "#e4e4e4",
        "selected-row": "#ffc",
        "button-fg": "#fff",
        "button-bg": "rgba(9,8,9,.6)",
        "button-hover-bg": "var(--secondary)",
        "default-button-bg": "rgba(9,8,9,.6)",
        "default-button-hover-bg": "var(--secondary)",
        "close-button-bg": "#747474",
        "close-button-hover-bg": "#333",
        "delete-button-bg": "#ba2121",
        "delete-button-hover-bg": "#a41515",
        "object-tools-fg": "var(--button-fg)",
        "object-tools-bg": "var(--close-button-bg)",
        "object-tools-hover-bg": "var(--close-button-hover-bg)",
      },
      boxShadow: {
        card: "0 10px 20px 0 rgba(0, 0, 0, 0.1)",
      },
      backgroundImage: {
        body: 'url("/static/images/background_texture.png")',
      },
    },
  },
  variants: {},
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
