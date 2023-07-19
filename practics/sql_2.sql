SELECT
  "Orders".track,
  CASE WHEN "Orders".finished THEN 2
       WHEN "Orders".canсelled THEN -1
       WHEN "Orders".inDelivery THEN 1
       ELSE 0
  END
FROM "Orders"
