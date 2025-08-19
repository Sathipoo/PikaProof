document.getElementById('download').addEventListener('click', function () {
    const element = document.getElementById('certificate');
    const opt = {
        margin:       0.5,
        filename:     'certificate.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' }
    };
    html2pdf().set(opt).from(element).save();
});
