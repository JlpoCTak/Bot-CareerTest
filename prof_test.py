import json

# earth_science = 0
# architecture = 0
# tech_and_technology_building = 0
# informatic = 0
# computer_security = 0
# electronic_radio = 0
# fotonic_biotech = 0
# electro_thermal_energetic = 0
# nuclear_energetic = 0
# machinary = 0
# chemistry_technology = 0
# industrial_echology_biotech = 0
# technosphere_safety_and_environmental_engineering = 0
# applied_geology_mining_oil_and_gas_engineering_and_geodesy = 0
# material_technologies = 0
# land_transportation_engineering_and_technology = 0
# aeronautical_and_rocket_space_engineering = 0
# aeronautical_navigation_and_operatio_of_aviation_and_rocket_space_equipment = 0
# engineering_and_technologies_of_shipbuilding_and_water_transport = 0
# control_in_technical_systems = 0
# light_industry_technologies = 0
# clinical_medicine = 0
# health_sciences_and_preventive_medicine = 0
# pharmacy = 0
# nursing = 0
# agriculture_forestry_and_fishery = 0
# veterinary_and_animal_science = 0
# economics_and_management = 0
# sociology_and_social_work = 0
# jurisprudence = 0
# media_and_information_librarianship = 0
# service_and_tourism = 0
# education_and_pedagogical_sciences = 0
# history_and_archaeology = 0
# physical_education_and_sport = 0
# art_history = 0
# cultural_studies_and_sociocultural_project = 0
# stage_arts_and_literary_arts = 0
# musical_art = 0
# fine_and_applied_arts = 0
# screen_arts = 0

def test_holland():
    with open('database/professions_for_text.json', 'r', encoding='utf-8') as profissions_text:
        with open('database/holland_table.json', 'r', encoding='utf-8') as holland_table:
            dict_prof = {'realistic': 0, 'intelligent': 0, 'social': 0, 'conventional': 0, 'enterprising': 0, 'artistic': 0}
            professions = json.load(profissions_text)
            hol_table = json.load(holland_table)
            for i in range(5):
                answer = f'{i+1}'+input()
                for a in hol_table:
                    if answer in hol_table[a]:
                        dict_prof[a]+=1
            print(max(dict_prof))
            print(dict_prof)


            # for section, commands in proffesions.items():
            #     print(i+1, section, commands)
            #     i+=1
            #     if i%2==0:
            #         print()

test_holland()

