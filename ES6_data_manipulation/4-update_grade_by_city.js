export default function updateStudentGradeByCity(students, city, newGrades) {
    const studentsByCity = students.filter(student => student.location === city)

    const studentsWGrades = studentsByCity.map(student => {
        let grade = 'N/A';
        for (const gradedStudent of newGrades) {
            if (student.id === gradedStudent.studentId) {
                grade = gradedStudent.grade;
            }
        }

        return {
            id: student.id,
            firstName: student.firstName,
            location: student.location,
            grade: grade
        };
    });

    return studentsWGrades
}
