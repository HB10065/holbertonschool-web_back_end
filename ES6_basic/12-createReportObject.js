export default function createReportObject(employeesList) {
    const report = {
        allEmployees: {},

        getNumberOfDepartments(employees) {
            return Object.keys(employees).length;
        }
    }

    for (let department in employeesList) {
        report.allEmployees[department] = employeesList[department]
    }

    return report
}
