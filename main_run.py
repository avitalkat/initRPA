import sys

# arguments
project_id = sys.argv[1]
file_name = sys.argv[2]



parser_type = ParserFactory.get_parser_type(file_type="regular")
parser_type(etl_id=etl_id,
            file_path=file_path,
            file_id=file_id,
            project_id=project_id,
            data=data).run()
