USE project_3_cleaning;

ALTER TABLE entrepreneurial_competency
ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

SELECT education_sector, ROUND(AVG(age))
FROM entrepreneurial_competency
GROUP BY education_sector
ORDER BY AVG(age);

SELECT id, education_sector, (perseverance + desire_to_take_initiative + competitiveness + self_reliance + strong_need_to_achieve + self_confidence + good_physical_health) AS score
FROM entrepreneurial_competency
ORDER BY score DESC;

SELECT education_sector, AVG(perseverance + desire_to_take_initiative + competitiveness + self_reliance + strong_need_to_achieve + self_confidence + good_physical_health) AS score
FROM entrepreneurial_competency
GROUP BY education_sector
ORDER BY score DESC;