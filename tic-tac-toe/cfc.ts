// Velo API Reference: https://www.wix.com/velo/reference/api-overview/introduction
import { authentication } from "wix-members-frontend";

// TODO:
// - Update primary member to have a secondary member field
// - Check to see that primary member doesn't have secondary email set already
// - Figure out a way to "tag" a newly registered member, so we know to add the secondary play for them
// - add secondary plan
// - update masterPage so the secondary doesn't hit a redirect

// Better option, figure out a way to check if the member is "tagged" on the master page, then optionally show member pages


$w.onReady(function () {
    $w("#form2").onSubmit(() => {
        const contact = $w("#form2").getFieldValues()
        const secondaryInfo = {
            firstName: contact["first_name"],
            lastName: contact["last_name"],
            emails: [contact["email"]],
            phones: [contact["phone"]],
        };

        const password = secondaryInfo.firstName + secondaryInfo.lastName
        const options = { contactInfo: secondaryInfo }
        const email = secondaryInfo.emails[0]

        authentication
            .register(email, password, options)
            .then((registrationResult) => {
                const status = registrationResult.status;
                if (status === "ACTIVE") {
                    console.log(
                        "Member registered and waiting for approval:",
                        registrationResult,
                    );
                } else {
                    console.log(
                        "Registration of new member not successful. Please contact the cfc tech team technology@coastsidefamilies.com",
                        registrationResult,
                    );
                }
            })
            .catch((error) => {
                console.error(error);
            })
    })
});