SELECT
    p.id AS patient_id,
    p.surgeon_id,
    s.name AS surgeon_name
FROM patients p
JOIN surgeons s ON p.surgeon_id = s.id