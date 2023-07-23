SELECT
  "Couriers".login,
  COUNT(*)
FROM "Couriers" 
LEFT JOIN "Orders" ON "Orders".courierId = "Couriers".id 
WHERE
  "Orders".inDelivery
GROUP BY "Couriers".login;
