# PromptPilot Portfolio Website

This is a fully static, visually striking portfolio website showcasing the PromptPilot AI-powered interview assistant application.

## Features

- **Animated Hero Section**: Features typed text effect and moving gradient backgrounds
- **Scroll-Triggered Animations**: Smooth fade-in animations as you scroll through sections
- **Interactive Project Cards**: Hover effects with elevation and scaling
- **Skills Progress Bars**: Animated progress indicators for technical skills
- **Contact Section**: Functional contact form with validation
- **Responsive Design**: Fully responsive layout that works on all devices
- **Download Buttons**: Links to download CV and Resume from Google Drive
- **Modern UI**: Built with Tailwind CSS via CDN for modern styling
- **Smooth Animations**: Subtle motion and hover effects throughout

## Usage

### Local Testing

1. Simply open `index.html` in a web browser
2. Or use a local server:
   ```bash
   cd portfolio
   python -m http.server 8080
   ```
   Then visit `http://localhost:8080` in your browser

### Customization

To customize the website:

1. **Update Download Links**: Replace `YOUR_CV_FILE_ID` and `YOUR_RESUME_FILE_ID` in the HTML with your actual Google Drive file IDs
2. **Modify Content**: Edit the text content directly in the HTML file
3. **Change Colors**: Tailwind CSS classes are used throughout - modify them as needed
4. **Add Projects**: Add more project cards in the Projects section

### Google Drive Setup

To set up the download buttons:

1. Upload your CV and Resume to Google Drive
2. Right-click the file and select "Get link"
3. Set permissions to "Anyone with the link can view"
4. Copy the file ID from the URL (the long string after `/d/` and before `/view`)
5. Replace `YOUR_CV_FILE_ID` and `YOUR_RESUME_FILE_ID` in the HTML

## Technologies

- HTML5
- Tailwind CSS (via CDN)
- Vanilla JavaScript
- Google Fonts (Inter)

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

## Note

The website uses CDN links for Tailwind CSS and Google Fonts. An internet connection is required for proper styling.
