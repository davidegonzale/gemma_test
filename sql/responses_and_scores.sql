SELECT
    a.patient_id,
    q.id AS questionnaire_id,
    q.type AS questionnaire_type,
    q.treatment,
    ao.central_estimate
FROM answers a
JOIN questionnaires q ON a.questionnaire_id = q.id
JOIN answer_options ao ON a.question_id = ao.question_id AND a.answer = ao.answer
WHERE q.treatment = 'Hip'
