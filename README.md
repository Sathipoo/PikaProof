# PikaProof
Flask-based application to generate internship certificates.

## Usage

1. Install dependencies:

```bash
pip install flask
```

2. Run the development server:

```bash
python app.py
```

3. Open the app in your browser at `http://localhost:5000`.

The home page provides a form view and a JSON input view. After submitting,
the certificate page allows downloading a PDF using `html2pdf.js`.
