import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";


export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
        .then((resutls) => {
            return resutls.map((result) => {
                if (result.status === 'fulfilled'){
                    return {
                        status: result.status,
                        value: result.value
                    }
                }
                if (result.status === 'rejected'){
                    return {
                        status: result.status,
                        value: result.reason.toString()
                    }
                }
            });
        });
}
