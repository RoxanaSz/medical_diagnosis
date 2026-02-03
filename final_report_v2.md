# ER Chest Pain – Decision Report

## Agent Outputs

### Cardiology Specialist


```json
{
  "hypothesis": "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain.",
  "confidence": 0.9,
  "supporting_findings": [
    "Unspecified chest pain presentation requiring urgent cardiac evaluation.",
    "Potential for typical anginal symptoms (substernal, radiating pain, exertional).",
    "Potential for associated symptoms like dyspnea, diaphoresis, nausea, syncope.",
    "Presence of cardiovascular risk factors (hypertension, diabetes, hyperlipidemia, smoking, family history) commonly associated with ACS.",
    "Absence of specific non-cardiac indicators based on available information, necessitating cardiac focus."
  ],
  "actions_recommended": [
    "Immediately obtain a 12-lead Electrocardiogram (ECG) to assess for ischemic changes (e.g., ST elevation/depression, T-wave inversion, new Q waves).",
    "Initiate serial cardiac troponin measurements (e.g., 0h/1h or 0h/3h protocol) to detect myocardial injury.",
    "Establish intravenous access and initiate cardiac monitoring.",
    "Administer aspirin (chewable) if not contraindicated.",
    "Administer nitroglycerin sublingually for pain relief if blood pressure is adequate and no contraindications (e.g., recent phosphodiesterase inhibitor use).",
    "Administer supplemental oxygen if hypoxemic (SpO2 < 90%) or in respiratory distress.",
    "Obtain a focused clinical history and physical examination, including vital signs, cardiac auscultation (murmurs, rubs), lung auscultation, and peripheral vascular assessment (e.g., bilateral blood pressures, pulse deficits).",
    "Consider a portable chest X-ray to assess for pulmonary edema, pneumothorax, or mediastinal widening (suggestive of aortic dissection).",
    "Prepare for further diagnostic imaging such as echocardiography to assess cardiac function, wall motion abnormalities, valvular disease, pericardial effusion, and aortic root dilation.",
    "If STEMI is identified, activate the cardiac catheterization lab for emergent revascularization.",
    "Consider advanced imaging like CT angiography of the chest if aortic dissection or pulmonary embolism remains a significant differential."
  ],
  "risk_if_missed": "High"
}
```

### Emergency Pulmonologist


```json
```json
{
  "hypothesis": "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features.",
  "confidence": 0.6,
  "alternative_diagnoses": [
    "Pulmonary Embolism (PE)",
    "Pneumothorax (spontaneous, traumatic, iatrogenic, tension)",
    "Pleurisy (due to viral infection, pneumonia, autoimmune disease, or malignancy)",
    "Pneumonia (especially with pleuritic pain or pleural effusion)",
    "Tracheobronchitis/Bronchitis",
    "Acute Exacerbation of Asthma/COPD (less common for primary chest pain)",
    "Esophageal Spasm",
    "Gastroesophageal Reflux Disease (GERD)/Esophagitis",
    "Esophageal Rupture (Boerhaave's syndrome)",
    "Peptic Ulcer Disease",
    "Gallbladder disease (biliary colic, referred pain)",
    "Pancreatitis",
    "Costochondritis/Tietze's syndrome",
    "Rib fracture/Contusion",
    "Intercostal muscle strain",
    "Cervical/Thoracic Radiculopathy",
    "Herpes Zoster (pre-eruptive phase)",
    "Anxiety/Panic Disorder",
    "Mediastinitis"
  ],
  "actions_recommended": [
    "Obtain a focused history inquiring about pleuritic nature of pain, positional changes, radiation, associated respiratory symptoms (cough, sputum, hemoptysis, dyspnea), risk factors for venous thromboembolism (e.g., recent surgery, immobilization, malignancy, oral contraceptives, prior VTE), gastrointestinal symptoms (dysphagia, heartburn, post-prandial pain), and musculoskeletal triggers (e.g., trauma, reproducible pain).",
    "Perform a thorough physical examination including careful lung auscultation for diminished breath sounds, crackles, rhonchi, wheezes, tactile fremitus, and dullness to percussion. Palpate the chest wall for tenderness, crepitus, and evaluate for unilateral leg swelling (DVT assessment for PE).",
    "Ensure an up-to-date Chest X-ray (CXR) has been performed and meticulously reviewed for evidence of pneumothorax, pleural effusion, pneumonia/infiltrates, rib fractures, mediastinal widening, or foreign body aspiration.",
    "Order a D-dimer test if the clinical pre-test probability for Pulmonary Embolism (PE) is low or intermediate (e.g., using Wells' or Geneva scoring systems) to rule out PE effectively.",
    "Obtain an Arterial Blood Gas (ABG) to assess for hypoxemia, hypercapnia, and acid-base status, especially if there is significant dyspnea or respiratory distress.",
    "Consider a Computed Tomography Pulmonary Angiography (CTPA) if PE is suspected based on elevated D-dimer and/or moderate-to-high pre-test probability, or if other pulmonary pathology requiring detailed imaging (e.g., mass, severe pneumonia) is suspected.",
    "If esophageal rupture (Boerhaave's syndrome) is suspected, consider an Esophagram with water-soluble contrast or a CT scan of the chest with oral contrast.",
    "Administer appropriate analgesia based on the suspected etiology (e.g., NSAIDs for pleuritic or musculoskeletal pain, opioids for severe pain).",
    "Initiate empiric antibiotics if pneumonia is highly suspected based on clinical presentation and imaging, pending culture results.",
    "Be prepared for immediate interventions such as chest tube insertion for tension pneumothorax or symptomatic large pleural effusion.",
    "Consider bronchodilators if reactive airway disease or exacerbation of COPD/asthma is a contributing factor to symptoms.",
    "If GI causes remain high on differential after cardiac and pulmonary workup, consider initiation of proton pump inhibitors (PPIs) and referral to Gastroenterology for further evaluation (e.g., endoscopy) if symptoms persist."
  ],
  "risk_if_missed": "High"
}
```
```

### Internal Medicine Physician


```json
{
  "hypothesis": "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies.",
  "confidence": 0.7,
  "conditions_not_ruled_out": [
    "Acute Coronary Syndrome (ACS)",
    "Acute Aortic Syndrome (Aortic Dissection, Intramural Hematoma, Penetrating Ulcer)",
    "Pulmonary Embolism (PE)",
    "Tension Pneumothorax or large spontaneous pneumothorax",
    "Esophageal Rupture (Boerhaave's syndrome)",
    "Pericardial Tamponade",
    "Severe Myocarditis/Pericarditis with hemodynamic compromise",
    "Severe Pneumonia with sepsis or respiratory failure",
    "Acute Pancreatitis with systemic complications"
  ],
  "actions_recommended": [
    "Conduct a thorough focused history to elicit characteristics suggestive of benign causes: reproducible pain with palpation or movement (musculoskeletal), relation to food or swallowing (GI), heartburn or regurgitation (GERD), recent stressors or panic attack history (anxiety).",
    "Perform a detailed physical examination including meticulous chest wall palpation for focal tenderness (costochondritis, muscle strain, rib fracture), assessment of dermatomal pain patterns (herpes zoster, radiculopathy), abdominal examination for epigastric or right upper quadrant tenderness, and careful auscultation for cardiac or pulmonary abnormalities.",
    "Review all initial diagnostic results (ECG, serial troponins, Chest X-ray, D-dimer if obtained) to confirm the low likelihood of acute cardiac or emergent pleuropulmonary pathology.",
    "Consider a trial of therapeutic interventions specific to benign causes: antacids or proton pump inhibitors (PPIs) for suspected GERD, NSAIDs or acetaminophen for musculoskeletal pain (if no contraindications).",
    "If anxiety/panic disorder is strongly suspected after excluding organic causes, provide reassurance and consider short-acting anxiolytics if indicated and appropriate.",
    "If gastrointestinal causes persist as a leading differential, consider focused laboratory tests (e.g., amylase, lipase, liver function tests) and potential referral for outpatient gastroenterology evaluation (e.g., endoscopy) if symptoms are recurrent or refractory.",
    "Educate the patient on the benign nature of their symptoms once serious conditions are adequately ruled out, provide discharge instructions, and advise on follow-up with primary care for ongoing management of specific conditions (e.g., chronic GERD, musculoskeletal pain).",
    "Maintain vigilance and continue to monitor for any changes in vital signs or clinical status that might suggest an evolving or previously unappreciated serious condition, until the patient is stable and discharged or transferred."
  ],
  "risk_if_missed": "High"
}
```

## Orchestrator Output

```json
[
  {
    "action": "Immediately obtain a 12-lead Electrocardiogram (ECG) to assess for ischemic changes (e.g., ST elevation/depression, T-wave inversion, new Q waves).",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Initiate serial cardiac troponin measurements (e.g., 0h/1h or 0h/3h protocol) to detect myocardial injury.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Establish intravenous access and initiate cardiac monitoring.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Administer aspirin (chewable) if not contraindicated.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Administer nitroglycerin sublingually for pain relief if blood pressure is adequate and no contraindications (e.g., recent phosphodiesterase inhibitor use).",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Administer supplemental oxygen if hypoxemic (SpO2 < 90%) or in respiratory distress.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Obtain a focused clinical history and physical examination, including vital signs, cardiac auscultation (murmurs, rubs), lung auscultation, and peripheral vascular assessment (e.g., bilateral blood pressures, pulse deficits).",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Consider a portable chest X-ray to assess for pulmonary edema, pneumothorax, or mediastinal widening (suggestive of aortic dissection).",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Prepare for further diagnostic imaging such as echocardiography to assess cardiac function, wall motion abnormalities, valvular disease, pericardial effusion, and aortic root dilation.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "If STEMI is identified, activate the cardiac catheterization lab for emergent revascularization.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Consider advanced imaging like CT angiography of the chest if aortic dissection or pulmonary embolism remains a significant differential.",
    "score": 0.9,
    "risk_coverage": [
      "Acute Coronary Syndrome (ACS) or other life-threatening cardiac pathology (e.g., acute aortic syndrome, pericardial tamponade) as the primary cause of chest pain."
    ]
  },
  {
    "action": "Conduct a thorough focused history to elicit characteristics suggestive of benign causes: reproducible pain with palpation or movement (musculoskeletal), relation to food or swallowing (GI), heartburn or regurgitation (GERD), recent stressors or panic attack history (anxiety).",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Perform a detailed physical examination including meticulous chest wall palpation for focal tenderness (costochondritis, muscle strain, rib fracture), assessment of dermatomal pain patterns (herpes zoster, radiculopathy), abdominal examination for epigastric or right upper quadrant tenderness, and careful auscultation for cardiac or pulmonary abnormalities.",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Review all initial diagnostic results (ECG, serial troponins, Chest X-ray, D-dimer if obtained) to confirm the low likelihood of acute cardiac or emergent pleuropulmonary pathology.",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Consider a trial of therapeutic interventions specific to benign causes: antacids or proton pump inhibitors (PPIs) for suspected GERD, NSAIDs or acetaminophen for musculoskeletal pain (if no contraindications).",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "If anxiety/panic disorder is strongly suspected after excluding organic causes, provide reassurance and consider short-acting anxiolytics if indicated and appropriate.",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "If gastrointestinal causes persist as a leading differential, consider focused laboratory tests (e.g., amylase, lipase, liver function tests) and potential referral for outpatient gastroenterology evaluation (e.g., endoscopy) if symptoms are recurrent or refractory.",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Educate the patient on the benign nature of their symptoms once serious conditions are adequately ruled out, provide discharge instructions, and advise on follow-up with primary care for ongoing management of specific conditions (e.g., chronic GERD, musculoskeletal pain).",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Maintain vigilance and continue to monitor for any changes in vital signs or clinical status that might suggest an evolving or previously unappreciated serious condition, until the patient is stable and discharged or transferred.",
    "score": 0.7,
    "risk_coverage": [
      "Benign or non-life-threatening causes of chest pain, such as musculoskeletal pain (e.g., costochondritis, muscle strain), gastrointestinal disorders (e.g., GERD, esophageal spasm), or anxiety/panic disorder, are the likely etiology after initial stabilization and preliminary exclusion of immediately life-threatening cardiac and acute pleuropulmonary pathologies."
    ]
  },
  {
    "action": "Obtain a focused history inquiring about pleuritic nature of pain, positional changes, radiation, associated respiratory symptoms (cough, sputum, hemoptysis, dyspnea), risk factors for venous thromboembolism (e.g., recent surgery, immobilization, malignancy, oral contraceptives, prior VTE), gastrointestinal symptoms (dysphagia, heartburn, post-prandial pain), and musculoskeletal triggers (e.g., trauma, reproducible pain).",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Perform a thorough physical examination including careful lung auscultation for diminished breath sounds, crackles, rhonchi, wheezes, tactile fremitus, and dullness to percussion. Palpate the chest wall for tenderness, crepitus, and evaluate for unilateral leg swelling (DVT assessment for PE).",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Ensure an up-to-date Chest X-ray (CXR) has been performed and meticulously reviewed for evidence of pneumothorax, pleural effusion, pneumonia/infiltrates, rib fractures, mediastinal widening, or foreign body aspiration.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Order a D-dimer test if the clinical pre-test probability for Pulmonary Embolism (PE) is low or intermediate (e.g., using Wells' or Geneva scoring systems) to rule out PE effectively.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Obtain an Arterial Blood Gas (ABG) to assess for hypoxemia, hypercapnia, and acid-base status, especially if there is significant dyspnea or respiratory distress.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Consider a Computed Tomography Pulmonary Angiography (CTPA) if PE is suspected based on elevated D-dimer and/or moderate-to-high pre-test probability, or if other pulmonary pathology requiring detailed imaging (e.g., mass, severe pneumonia) is suspected.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "If esophageal rupture (Boerhaave's syndrome) is suspected, consider an Esophagram with water-soluble contrast or a CT scan of the chest with oral contrast.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Administer appropriate analgesia based on the suspected etiology (e.g., NSAIDs for pleuritic or musculoskeletal pain, opioids for severe pain).",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Initiate empiric antibiotics if pneumonia is highly suspected based on clinical presentation and imaging, pending culture results.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Be prepared for immediate interventions such as chest tube insertion for tension pneumothorax or symptomatic large pleural effusion.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "Consider bronchodilators if reactive airway disease or exacerbation of COPD/asthma is a contributing factor to symptoms.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  },
  {
    "action": "If GI causes remain high on differential after cardiac and pulmonary workup, consider initiation of proton pump inhibitors (PPIs) and referral to Gastroenterology for further evaluation (e.g., endoscopy) if symptoms persist.",
    "score": 0.6,
    "risk_coverage": [
      "Pulmonary Embolism (PE), Pneumothorax, or other acute pleuropulmonary pathology (e.g., pneumonia with pleurisy, pleural effusion) as a significant cause of chest pain, particularly in the context of a potentially non-diagnostic cardiac workup or atypical cardiac features."
    ]
  }
]
```
