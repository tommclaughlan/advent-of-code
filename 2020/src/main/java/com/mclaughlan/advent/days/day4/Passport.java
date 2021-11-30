package com.mclaughlan.advent.days.day4;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Passport {
    private String birthYear;
    private String issueYear;
    private String expirationYear;
    private String height;
    private String hairColour;
    private String eyeColour;
    private String passportId;
    private String countryId;

    public Passport(String passportString) {
        var map = Arrays.stream(passportString.split(" "))
                .map(i -> i.split(":"))
                .collect(Collectors.toMap(i -> i[0], i -> i[1]));
        birthYear = map.get("byr");
        issueYear = map.get("iyr");
        expirationYear = map.get("eyr");
        height = map.get("hgt");
        hairColour = map.get("hcl");
        eyeColour = map.get("ecl");
        passportId = map.get("pid");
        countryId = map.get("cid");
    }

    public boolean isValid() {
        return birthYear != null &&
                issueYear != null &&
                expirationYear != null &&
                height != null &&
                hairColour != null &&
                eyeColour != null &&
                passportId != null;
    }

    public boolean isValidStrict() {
        return  validBirthYear() &&
                validIssueYear() &&
                validExpirationYear() &&
                validHeight() &&
                validHairColour() &&
                validEyeColour() &&
                validPassportId();
    }

    private boolean validBirthYear() {
        try {
            return validateYear(birthYear, 1920, 2002);
        } catch (Exception e) {
            return false;
        }
    }

    private boolean validIssueYear() {
        try {
            return validateYear(issueYear, 2010, 2020);
        } catch (Exception e) {
            return false;
        }
    }

    private boolean validExpirationYear() {
        try {
            return validateYear(expirationYear, 2020, 2030);
        } catch (Exception e) {
            return false;
        }
    }

    private boolean validHeight() {
        if (height == null) {
            return false;
        }

        if (height.contains("cm")) {
            return validateRange(height.replace("cm", ""), 150, 193);
        } else if (height.contains("in")) {
            return validateRange(height.replace("in", ""), 59, 76);
        }

        return false;
    }

    private boolean validHairColour() {
        return hairColour != null && hairColour.matches("^\\#[0-9a-f]{6}+$") && hairColour.length() == 7;
    }

    private boolean validEyeColour() {
        return eyeColour != null && eyeColour.matches("^amb|blu|brn|gry|grn|hzl|oth$");
    }

    private boolean validPassportId() {
        return passportId != null && passportId.matches("^\\d{9}$");
    }

    private boolean validateYear(String test, int low, int high) {
        return validateRange(test, low, high) && test.length() == 4;
    }

    private boolean validateRange(String test, int low, int high) {
        try {
            var year = Integer.parseInt(test);
            return low <= year && year <= high;
        } catch (Exception e) {
            return false;
        }
    }
}
