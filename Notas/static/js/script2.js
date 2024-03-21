const grades = [
    { subject: 'Mathematics', accumulatedGrade: 85, evaluatedPercentage: 75 },
    { subject: 'Science', accumulatedGrade: 90, evaluatedPercentage: 80 },
    { subject: 'English', accumulatedGrade: 80, evaluatedPercentage: 70 },
    { subject: 'Spanish', accumulatedGrade: 95, evaluatedPercentage: 90 },
    { subject: 'History', accumulatedGrade: 75, evaluatedPercentage: 65 },
    { subject: 'Physical Education', accumulatedGrade: 92, evaluatedPercentage: 85 },
];

const gradesTableBody = document.querySelector('.grades-table tbody');

grades.forEach(grade => {
    const row = document.createElement('tr');

    const subjectCell = document.createElement('td');
    subjectCell.textContent = grade.subject;
    row.appendChild(subjectCell);

    const accumulatedGradeCell = document.createElement('td');
    accumulatedGradeCell.textContent = grade.accumulatedGrade;
    row.appendChild(accumulatedGradeCell);

    const evaluatedPercentageCell = document.createElement('td');
    evaluatedPercentageCell.textContent = grade.evaluatedPercentage;
    row.appendChild(evaluatedPercentageCell);

    gradesTableBody.appendChild(row);
});